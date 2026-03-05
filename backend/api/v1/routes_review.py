from fastapi import APIRouter
from pydantic import BaseModel
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse
from core.logging import logger

# Import service layer functions (implemented by Dev C)
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai, llm_suggestions
from services.scoring_service import calculate_score


# Create router for review-related APIs
router = APIRouter(prefix="/review", tags=["Code Review"])

class CodeRequest(BaseModel):
    code: str


# Main API endpoint to submit code for review
@router.post(
    "",
    response_model=CodeReviewResponse,  # Ensures response follows schema
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

        # Step 3: Generate AI-based suggestions using Phi3 Mini model
        logger.info("Generating LLM suggestions")
        llm_suggestions = llm_suggestions(code, result)

        # Step 4: Calculate quality score for the code
        logger.info("Calculating score")
        score = calculate_score(result)

        # Return combined result back to client
        return {
            "status": "success",
            "analysis": result,
            "rule_based_suggestions": rule_suggestions,
            "llm_suggestions": llm_suggestions,
            "score": score
        }

    # Handle unexpected errors
    except Exception as e:

        logger.error(f"Code review failed: {str(e)}")

        return {
            "status": "error",
            "message": "Failed to process code review request"
        }


# Secondary endpoint used for direct analysis testing

@router.post("/analyze")
def analyze_endpoint(request: CodeRequest):
    result = analyze_code(request.code)
    rule_suggestions = rule_based_ai(result)
    llm_output = llm_suggestions(request.code)
    score = calculate_score(result)
    return {
        "analysis": result,
        "rule_based_suggestions": rule_suggestions,
        "llm_suggestions": llm_output,
        "score": score
    }
