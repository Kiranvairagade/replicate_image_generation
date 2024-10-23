from pydantic import BaseModel
from typing import List

class ImageGenerationRequest(BaseModel):
    prompt: str
    num_images: int = 1

class ImageResponse(BaseModel):
    images: List[str]
