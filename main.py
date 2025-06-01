import os
import time
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

from charlie_image_generator import root_agent

# Load environment variables first - ADK automatically finds API keys
load_dotenv()

# Set up simplified logging
def setup_logging():
    # Use stdout-only logging for Docker deployment
    # Docker captures stdout logs, accessible via 'docker logs'
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.StreamHandler()  # stdout only
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# Initialize FastAPI app
app = FastAPI(
    title="Charlie Image Generator API",
    description="API for generating images of Charlie using an ADK agent pipeline and fal.ai integration",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ADK components for agent execution
# InMemorySessionService: Stores conversation state temporarily
# Runner: Executes the agent pipeline and manages events
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,  # Root coordinator agent from agent.py
    app_name="charlie_image_generator",
    session_service=session_service
)

class GenerationRequest(BaseModel):
    prompt: str

class GenerationResponse(BaseModel):
    image_url: str

@app.get("/")
async def read_root():
    return {"status": "online", "service": "Charlie Image Generator"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/generate")
async def generate_image(request: GenerationRequest):
    request_id = f"req_{hash(request.prompt) % 10000:04d}"
    start_time = time.time()

    try:

        # Create unique session for this request
        # Each request gets isolated state to avoid cross-contamination
        session_id = f"session_{id(request)}"
        session = session_service.create_session(
            app_name="charlie_image_generator",
            user_id="user",  # Static user for microservice context
            session_id=session_id
        )

        # Convert user prompt to ADK message format
        # Content.parts can contain text, images, or function calls
        message_content = types.Content(
            role="user", 
            parts=[types.Part(text=request.prompt)]
        )

        # Execute agent pipeline and collect all events
        # Events contain agent communications, function calls, and responses
        events = []
        async for event in runner.run_async(
            user_id="user",
            session_id=session_id,
            new_message=message_content
        ):
            events.append(event)

        # Parse events to extract image URL and log agent communications
        # Events can contain state_delta, function responses, or content parts
        found_image_url = None

        # Log initial user message for debugging
        logger.info(f"[{request_id}] 📝 User → Root Agent: '{request.prompt}'")

        for event in events:
            try:
                # Check state_delta for agent outputs (ADK's output_key mechanism)
                # Each sub-agent stores results using their output_key
                if event.actions and event.actions.state_delta:
                    state = event.actions.state_delta

                    # Log pipeline progression through Writer → Reviewer → Refiner
                    if 'initial_prompt' in state:
                        logger.info(f"[{request_id}] ✍️  Writer Agent: '{state['initial_prompt']}'")
                    if 'review_feedback' in state:
                        logger.info(f"[{request_id}] 📋 Reviewer Agent: {state['review_feedback']}")
                    if 'final_prompt' in state:
                        logger.info(f"[{request_id}] 🎨 Refiner Agent: '{state['final_prompt']}'")

                # Check content parts for agent text responses and function calls
                # Events can have multiple parts (text + function calls)
                if event.content and event.content.parts:
                    for i, part in enumerate(event.content.parts):

                        # Log text responses from root agent (when it responds directly to user)
                        if part.text and event.author == 'charlie_image_generator':
                            logger.info(f"[{request_id}] 🤖 Root Agent → User [part {i}]: '{part.text}'")

                        # Log function calls from root agent
                        if part.function_call:
                            if part.function_call.name == 'prompt_pipeline_agent':
                                request_text = part.function_call.args.get('request', '')
                                logger.info(f"[{request_id}] 🤖 Root Agent → Pipeliine Agent [part {i}]: '{request_text}'")
                            elif part.function_call.name == 'generate_image':
                                prompt_arg = part.function_call.args.get('prompt', '')
                                logger.info(f"[{request_id}] 🤖 Root Agent → Generate Tool [part {i}]: '{prompt_arg}'")

                        # Check function responses - most reliable source for image URL
                        # fal.ai API returns image_url directly in function response
                        elif part.function_response and part.function_response.name == 'generate_image':
                            response = part.function_response.response
                            logger.info(f"[{request_id}] 🔧 Generate Tool → Root Agent [part {i}]: {response}")
                            if response.get('status') == 'success' and 'image_url' in response:
                                found_image_url = response['image_url']
                                logger.info(f"[{request_id}] ✅ Image URL found in function response")
                                # Continue parsing to capture complete flow

                # Process final agent response and extract fallback image URL
                # is_final_response() indicates the agent has completed its task
                if event.is_final_response():
                    logger.info(f"[{request_id}] 🗨️ Final Response:")

                    # Log final text response (check all parts)
                    if event.content and event.content.parts:
                        for i, part in enumerate(event.content.parts):
                            if part.text:
                                logger.info(f"[{request_id}]   Text [part {i}]: '{part.text}'")
                            else:
                                logger.info(f"[{request_id}]   Text [part {i}]: (no text)")

                    # Log final state_delta (output_key results)
                    if event.actions and event.actions.state_delta:
                        final_state = event.actions.state_delta
                        logger.info(f"[{request_id}]   State: {final_state}")

                        # Use state_delta as fallback if function response failed
                        # Root agent's output_key="image_url" stores result here
                        if not found_image_url and 'image_url' in final_state:
                            found_image_url = final_state['image_url']
                            logger.info(f"[{request_id}] ✅ Image URL found in final state_delta")

                    break  # Final response processed, exit event loop

            except AttributeError:
                # Skip malformed events
                continue

        if found_image_url:
            elapsed_time = time.time() - start_time
            logger.info(f"[{request_id}] ✅ Completed in {elapsed_time:.1f} seconds")
            return GenerationResponse(image_url=found_image_url)

        # If we get here, no image_url was found anywhere
        elapsed_time = time.time() - start_time
        logger.error(f"[{request_id}] ❌ No image_url found in any event location (after {elapsed_time:.1f} seconds)")
        raise HTTPException(status_code=500, detail="Failed to generate image")

    except Exception as e:
        elapsed_time = time.time() - start_time
        logger.error(f"[{request_id}] 💥 Error after {elapsed_time:.1f} seconds: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: 500: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
