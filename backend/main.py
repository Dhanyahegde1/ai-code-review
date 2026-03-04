from fastapi import FastAPI
from config import get_settings
from api.v1.routes_review import router as review_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }

@app.get("/")
async def root():
    return {"message": "AI Code Review Backend is running"}

# Register Review API Router
app.include_router(
    review_router,
    prefix="/api/v1",
    tags=["Code Review"]
)