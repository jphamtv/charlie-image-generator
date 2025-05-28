import os
import logging
import asyncio
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

# Set up logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

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
    try:
        # Create a unique session ID for this request
        session_id = f"session_{id(request)}"
        logger.info(f"Starting image generation for session {session_id}")
        
        # Create session for this request
        session = session_service.create_session(
            app_name="charlie_image_generator",
            user_id="user",
            session_id=session_id
        )
        
        # Create the user message content
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
        
        # Extract image URL from state_delta (cleanest approach)
        # The output_key="image_url" stores the result in actions.state_delta.image_url
        
        # Extract image URL from state_delta (cleanest approach)
        # The output_key="image_url" stores the result in actions.state_delta['image_url']
        for event in reversed(events):
            if (hasattr(event, 'actions') and event.actions and 
                hasattr(event.actions, 'state_delta') and event.actions.state_delta and
                isinstance(event.actions.state_delta, dict) and 'image_url' in event.actions.state_delta):
                image_url = event.actions.state_delta['image_url']
                logger.info(f"Generated image URL: {image_url}")
                return GenerationResponse(image_url=image_url)
        
        # If we get here, we couldn't find an image URL in state_delta
        logger.error(f"No image URL found in state_delta from {len(events)} events")
        raise HTTPException(status_code=500, detail="Failed to generate image")
    
    except Exception as e:
        logger.error(f"Error generating image: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error generating image: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
