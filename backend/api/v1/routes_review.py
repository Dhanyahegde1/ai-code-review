from fastapi import APIRouter
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse
from core.logging import logger

from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai, phi3_mini_ai
from services.scoring_service import calculate_score

router = APIRouter(prefix="/review", tags=["Code Review"])


@router.post(
    "",
    response_model=CodeReviewResponse,
    summary="Submit code for AI review",
    description="Runs analyzer, AI suggestions and scoring."
)
async def review_code(request: CodeReviewRequest):

    logger.info("Received code review request")

    try:
        code = request.code

        logger.info("Running analyzer")
        result = analyze_code(code)

        logger.info("Generating rule-based suggestions")
        rule_suggestions = rule_based_ai(result)

        logger.info("Generating LLM suggestions")
        llm_suggestions = phi3_mini_ai(code, result)

        logger.info("Calculating score")
        score = calculate_score(result)

        return {
            "status": "success",
            "analysis": result,
            "rule_based_suggestions": rule_suggestions,
            "llm_suggestions": llm_suggestions,
            "score": score
        }

    except Exception as e:
        logger.error(f"Code review failed: {str(e)}")

        return {
            "status": "error",
            "message": "Failed to process code review request"
        }


@router.post("/analyze")
def analyze_endpoint(request: CodeReviewRequest):

    result = analyze_code(request.code)
    rule_suggestions = rule_based_ai(result)
    llm_suggestions = phi3_mini_ai(request.code, result)
    score = calculate_score(result)

    return {
        "analysis": result,
        "rule_based_suggestions": rule_suggestions,
        "llm_suggestions": llm_suggestions,
        "score": score
    }