from fastapi import APIRouter
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse
from core.logging import logger

router = APIRouter()


@router.post("/review", response_model=CodeReviewResponse)
async def review_code(request: CodeReviewRequest):

    logger.info("Received code review request")

    try:
        code = request.code

        logger.info("Code snippet received for analysis")

        # Placeholder for Dev C modules
        logger.info("Waiting for analyzer and AI modules")

        return {
            "message": "Review endpoint ready for analyzer integration",
            "status": "waiting_for_dev_c_modules"
        }

    except Exception as e:
        logger.error(f"Code review failed: {str(e)}")

        return {
            "message": "Error processing code review",
            "status": "failed"
        }