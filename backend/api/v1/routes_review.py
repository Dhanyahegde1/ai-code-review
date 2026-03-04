from fastapi import APIRouter
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse
from core.logging import logger

router = APIRouter()


@router.post(
    "/review",
    response_model=CodeReviewResponse,
    summary="Submit code for AI review",
    description="Accepts a code snippet and prepares it for analysis by the code analyzer and AI engine."
)
async def review_code(request: CodeReviewRequest):

    logger.info("Received code review request")

    try:
        code = request.code

        logger.info("Code snippet received for analysis")

        # Placeholder until Dev C integrates analyzer
        logger.info("Analyzer and AI modules not integrated yet")

        return {
            "status": "success",
            "message": "Review endpoint ready. Waiting for analyzer integration."
        }

    except Exception as e:
        logger.error(f"Code review failed: {str(e)}")

        return {
            "status": "error",
            "message": "Failed to process code review request"
        }