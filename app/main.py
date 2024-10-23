from fastapi import FastAPI
from app.routers import image

app = FastAPI(title="Image Generation API", version="1.0")

app.include_router(image.router, prefix="/api/images")

@app.get("/", summary="Root endpoint")
async def root():
    return {"message": "Welcome to the Image Generation API"}
