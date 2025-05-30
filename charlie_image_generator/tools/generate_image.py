import asyncio
import fal_client
import logging

logger = logging.getLogger(__name__)

async def generate_image_with_retry(prompt: str, max_retries: int = 3) -> dict:
    """Generate image with retry logic."""
    
    for attempt in range(max_retries):
        try:
            logger.info(f"fal.ai attempt {attempt + 1}/{max_retries}")
            
            handler = await fal_client.submit_async(
                "fal-ai/flux-lora",
                arguments={
                    "prompt": prompt,
                    "loras": [{"path": "jtvp/chrle-flux.1-lora", "scale": 1}],
                    "embeddings": [],
                    "output_format": "jpeg",
                    "guidance_scale": 3.5,
                    "num_inference_steps": 28,
                    "enable_safety_checker": False,
                    "image_size": "square_hd",
                },
            )

            # Get result without detailed progress logging
            async for event in handler.iter_events():
                pass  # Just consume events

            result = await handler.get()
            image_url = result["images"][0]["url"]
            
            logger.info(f"fal.ai success on attempt {attempt + 1}")
            return {"status": "success", "image_url": image_url}

        except Exception as e:
            logger.warning(f"fal.ai attempt {attempt + 1} failed: {str(e)}")
            
            if attempt == max_retries - 1:
                logger.error(f"All {max_retries} attempts failed")
                return {"status": "error", "error_message": f"Failed after {max_retries} attempts: {str(e)}"}
            
            # Exponential backoff: 2s, 4s, 8s
            wait_time = 2 ** attempt
            logger.info(f"Waiting {wait_time}s before retry...")
            await asyncio.sleep(wait_time)

async def generate_image(prompt: str) -> dict:
    """Generates an image of Charlie using the final_prompt.

    Args:
        final_prompt: The prompt to generate the image.

    Returns:
        A dictionary containing the status and the image_url.
        Possible statuses: 'success', 'error'.
        Example success: {'status': 'success', 'image_url': 'https...'}
        Example error: {'status': 'error', 'error_message': 'Failed after 3 attempts: ...'}
    """
    return await generate_image_with_retry(prompt, max_retries=3)

if __name__ == "__main__":
    # For testing
    prompt = "ultra realistic photo, small (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, one ear up, playing in snow"
    result = asyncio.run(generate_image(prompt))
    print(result)
