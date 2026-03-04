from fastapi import APIRouter
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse

router = APIRouter()


@router.post("/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):
    return {
        "message": "Review endpoint skeleton ready",
        "status": "pending integration"
    }