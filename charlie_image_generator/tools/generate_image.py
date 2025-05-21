import asyncio
import fal_client
import logging

BASE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
LORA_PATH = "jtvp/chrle-lora-07"
NEGATIVE_PROMPT = """ugly, tiling, poorly drawn paws, poorly drawn face, out of 
frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, 
watermark, signature, cut off, low contrast, underexposed, overexposed, bad 
art, beginner, amateur, blurry, jpeg artifacts, mutated hands, poorly drawn 
hands, malformed limbs, extra fingers, text, logo, username, missing limbs, 
human-like eyes, scary, aggressive, contorted, unnatural pose, disproportionate 
body, unrealistic fur texture"""

logger = logging.getLogger(__name__)

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            logger.info(f"fal.ai: {log['message']}")

async def generate_image_async(prompt: str) -> dict:
    """Generate an image of Charlie using fal.ai with the LORA model.
    
    Args:
        prompt: The refined prompt to use for image generation
        
    Returns:
        dict: A dictionary containing the status and image URL
    """
    try:
        logger.info(f"Generating image with prompt: {prompt}")
        handler = await fal_client.submit_async(
            "fal-ai/lora",
            arguments={
                "model_name": BASE_MODEL,
                "prompt": prompt,
                "negative_prompt": NEGATIVE_PROMPT,
                "prompt_weighting": True,
                "loras": [{"path": LORA_PATH, "scale": 0.7}],
                "image_size": "square_hd",
                "num_inference_steps": 26,
                "guidance_scale": 0.7,
                "image_format": "jpeg",
                "scheduler": "DPM++ 2M Karras",
            },
            with_logs=True,
            on_queue_update=on_queue_update,
        )

        async for event in handler.iter_events(with_logs=True):
            logger.debug(f"Event: {event}")

        result = await handler.get()
        image_url = result.data.image[0].url

        logger.info(f"Generated image URL: {image_url}")
        return {"status": "success", "image_url": image_url}
    
    except Exception as e:
        logger.error(f"Error generating image: {str(e)}", exc_info=True)
        return {"status": "error", "error_message": str(e)}

def generate_image(prompt: str) -> dict:
    """Generate an image of Charlie using fal.ai with the LORA model.
    
    This function serves as a synchronous wrapper around the async implementation.
    
    Args:
        prompt: The refined prompt to use for image generation
        
    Returns:
        dict: A dictionary containing the status and image URL
    """
    try:
        # Run the async function in a synchronous context
        return asyncio.run(generate_image_async(prompt))
    except Exception as e:
        logger.error(f"Error in generate_image: {str(e)}", exc_info=True)
        return {"status": "error", "error_message": str(e)}

if __name__ == "__main__":
    # For testing
    prompt = "ultra realistic photo, small (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, one ear up, playing in snow"
    result = generate_image(prompt)
    print(result)
