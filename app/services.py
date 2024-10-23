import httpx
from app.config import settings
from app.schemas import ImageGenerationRequest, ImageResponse

async def generate_images(request: ImageGenerationRequest) -> ImageResponse:
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Bearer {settings.REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "version": "22.04",
        "input": {
            "prompt": request.prompt,
            "num_images": request.num_images
        }
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()
        
    return ImageResponse(images=[output['url'] for output in response_data['output']])
