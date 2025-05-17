import asyncio
import fal_client


async def subscribe():
    handler = await fal_client.submit_async(
        "fal-ai/lora",
        arguments={
            "model_name": "stabilityai/stable-diffusion-xl-base-1.0",
            "prompt": "Photo of a european medieval 40 year old queen, silver hair, highly detailed face, detailed eyes, head shot, intricate crown, age spots, wrinkles",
            "negative_prompt": "blurry, distorted",
            "prompt_weighting": true,
            "loras": [jtvp/chrle-lora-07],
            "path": "jtvp/chrle-lora-07"
            "scale": 0.7,
            "num_inference_steps": 26,
            "guidance_scale": 7,
            "scheduler": "DPM++ 2M Karras",
            "image_format": "jpeg"
        },
    )

    async for event in handler.iter_events(with_logs=True):
        print(event)

    result = await handler.get()

    print(result)


if __name__ == "__main__":
    asyncio.run(subscribe())
