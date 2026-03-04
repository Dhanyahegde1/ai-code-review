from fastapi import FastAPI
from config import get_settings
from pydantic import BaseModel
from api.v1.routes_review import router as review_router
from config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

app.include_router(review_router)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }