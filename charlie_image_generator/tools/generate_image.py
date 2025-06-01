import asyncio
import fal_client
import logging
import os

logger = logging.getLogger(__name__)

lora_path = os.getenv("LORA_PATH")

async def generate_image_with_retry(prompt: str, max_retries: int = 3) -> dict:
    """Generate image with retry logic."""
    
    for attempt in range(max_retries):
        try:
            logger.info(f"fal.ai attempt {attempt + 1}/{max_retries}")
            
            handler = await fal_client.submit_async(
                "fal-ai/flux-lora",
                arguments={
                    "prompt": prompt,
                    "loras": [{"path": lora_path, "scale": 1}],
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
            
            # Exponential backoff: 2s, 4s, 8s intervals
            wait_time = 2 ** attempt
            logger.info(f"Waiting {wait_time}s before retry...")
            await asyncio.sleep(wait_time)

async def generate_image(prompt: str) -> dict:
    """Main image generation function called by root coordinator agent.
    
    This function is exposed as a tool to the root coordinator agent.
    It wraps the retry logic and provides a clean interface.

    Args:
        prompt: Optimized prompt from the pipeline agent

    Returns:
        Dict with 'status' and either 'image_url' or 'error_message'
        Success: {'status': 'success', 'image_url': 'https://...'}
        Failure: {'status': 'error', 'error_message': 'Failed after 3 attempts: ...'}
    """
    return await generate_image_with_retry(prompt, max_retries=3)

if __name__ == "__main__":
    # For testing
    prompt = "ultra realistic photo, small (chrle:1.1), brown fur, milk chocolate color nose, intelligent light brown eyes, one ear up, playing in snow"
    result = asyncio.run(generate_image(prompt))
    print(result)
