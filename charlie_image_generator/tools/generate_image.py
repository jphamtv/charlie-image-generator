import asyncio
import fal_client

BASE_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
LORA_PATH = "jtvp/chrle-lora-07"
NEGATIVE_PROMPT = """ugly, tiling, poorly drawn paws, poorly drawn face, out of 
frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, 
watermark, signature, cut off, low contrast, underexposed, overexposed, bad 
art, beginner, amateur, blurry, jpeg artifacts, mutated hands, poorly drawn 
hands, malformed limbs, extra fingers, text, logo, username, missing limbs, 
human-like eyes, scary, aggressive, contorted, unnatural pose, disproportionate 
body, unrealistic fur texture"""


def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(log["message"])


async def subscribe(prompt: str) -> object:
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
        print(event)

    result = await handler.get()
    image_url = result.data.image[0].url

    print(image_url)

if __name__ == "__main__":
    asyncio.run(subscribe())
