import asyncio
import fal_client
import logging

LORA_PATH = "jtvp/chrle-flux.1-lora" # huggingface model path

logger = logging.getLogger(__name__)

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
            "fal-ai/flux-lora",
            arguments={
                "prompt": prompt,
                # "model_name": null,
                "loras": [
                    {
                        "path": "jtvp/chrle-flux.1-lora",
                        "scale": 1,
                    }
                ],
                "embeddings": [],
                "output_format": "jpeg",
                "guidance_scale": 3.5,
                "num_inference_steps": 28,
                "image_size": "square_hd",
            },
        )

        # Monitor progress and get logs
        async for event in handler.iter_events(with_logs=True):
            if hasattr(event, 'logs'):
                for log in event.logs:
                    logger.info(f"fal.ai: {log.get('message', str(log))}")
            logger.debug(f"Event: {event}")

        result = await handler.get()
        image_url = result["images"][0]["url"]

        logger.info(f"Generated image URL: {image_url}")
        return {"status": "success", "image_url": image_url}

    except Exception as e:
        logger.error(f"Error generating image: {str(e)}", exc_info=True)
        return {"status": "error", "error_message": str(e)}

async def generate_image(prompt: str) -> dict:
    """Generate an image of Charlie using fal.ai with the LORA model.
    
    Args:
        prompt: The refined prompt to use for image generation
        
    Returns:
        dict: A dictionary containing the status and image URL
    """
    return await generate_image_async(prompt)

if __name__ == "__main__":
    # For testing
    prompt = "ultra realistic photo, small (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, one ear up, playing in snow"
    result = asyncio.run(generate_image(prompt))
    print(result)
