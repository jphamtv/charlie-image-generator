import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

from charlie_image_generator import root_agent

# Load environment variables
load_dotenv()

# Set up simplified logging
def setup_logging():
    log_dir = Path("/app/logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                log_dir / "charlie.log",
                maxBytes=5*1024*1024,  # 5MB
                backupCount=2
            )
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

# Initialize session service and runner with the root agent
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
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

    try:

        # Create session
        session_id = f"session_{id(request)}"
        session = session_service.create_session(
            app_name="charlie_image_generator",
            user_id="user",
            session_id=session_id
        )

        # Create message content
        message_content = types.Content(
            role="user", 
            parts=[types.Part(text=request.prompt)]
        )

        events = []
        async for event in runner.run_async(
            user_id="user",
            session_id=session_id,
            new_message=message_content
        ):
            events.append(event)

        # Parse events for agent communications and extract image URL
        found_image_url = None

        # Log user's message
        logger.info(f"[{request_id}] 📝 User → Root Agent: '{request.prompt}'")

        for event in events:
            try:
                # Check actions.state_delta for agent outputs
                if event.actions and event.actions.state_delta:
                    state = event.actions.state_delta

                    # Log pipeline outputs
                    if 'initial_prompt' in state:
                        logger.info(f"[{request_id}] ✍️  Writer Agent: '{state['initial_prompt']}'")
                    if 'review_feedback' in state:
                        logger.info(f"[{request_id}] 📋 Reviewer Agent: {state['review_feedback']}")
                    if 'final_prompt' in state:
                        logger.info(f"[{request_id}] 🎨 Refiner Agent: '{state['final_prompt']}'")

                # Check content parts (iterate through all parts, not just parts[0])
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

                        # Check function responses (most reliable source for image URL)
                        elif part.function_response and part.function_response.name == 'generate_image':
                            response = part.function_response.response
                            logger.info(f"[{request_id}] 🔧 Generate Tool → Root Agent [part {i}]: {response}")
                            if response.get('status') == 'success' and 'image_url' in response:
                                found_image_url = response['image_url']
                                logger.info(f"[{request_id}] ✅ Image URL found in function response")
                                # Don't break here, continue to log final response

                # Log final response from root agent
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

                        # Use state_delta as fallback for image_url
                        if not found_image_url and 'image_url' in final_state:
                            found_image_url = final_state['image_url']
                            logger.info(f"[{request_id}] ✅ Image URL found in final state_delta")

                    break  # Final response found, exit loop

            except AttributeError:
                # Skip malformed events
                continue

        if found_image_url:
            logger.info(f"[{request_id}] ✅ Complete")
            return GenerationResponse(image_url=found_image_url)

        # If we get here, no image_url was found anywhere
        logger.error(f"[{request_id}] ❌ No image_url found in any event location")
        raise HTTPException(status_code=500, detail="Failed to generate image")

    except Exception as e:
        logger.error(f"[{request_id}] 💥 Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error: 500: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
