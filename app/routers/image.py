from fastapi import APIRouter, HTTPException
from app.schemas import ImageGenerationRequest, ImageResponse
from app.services import generate_images

router = APIRouter()

@router.post("/generate", response_model=ImageResponse, summary="Generate images based on a prompt")
async def generate_image(request: ImageGenerationRequest):
    try:
        return await generate_images(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
