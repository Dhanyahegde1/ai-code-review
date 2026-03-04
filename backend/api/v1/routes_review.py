# Import FastAPI router to create API endpoints
from fastapi import APIRouter

# Import request and response schemas for validation
from schemas.review_schema import CodeReviewRequest, CodeReviewResponse

# Import centralized logging system
from core.logging import logger

# Import service layer functions (implemented by Dev C)
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai, phi3_mini_ai
from services.scoring_service import calculate_score


# Create router for review-related APIs
# All routes here will start with /review
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

    # Log that a new request has been received
    logger.info("Received code review request")

    try:
        # Extract the code from request body
        code = request.code

        # Step 1: Analyze the code using static analyzer
        logger.info("Running analyzer")
        result = analyze_code(code)

        # Step 2: Generate rule-based suggestions
        logger.info("Generating rule-based suggestions")
        rule_suggestions = rule_based_ai(result)

        # Step 3: Generate AI-based suggestions using Phi3 Mini model
        logger.info("Generating LLM suggestions")
        llm_suggestions = phi3_mini_ai(code, result)

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

        # Log the error message
        logger.error(f"Code review failed: {str(e)}")

        # Return error response
        return {
            "status": "error",
            "message": "Failed to process code review request"
        }


# Secondary endpoint used for direct analysis testing
# Useful during development for testing analyzer and AI modules
@router.post("/analyze")
def analyze_endpoint(request: CodeReviewRequest):

    # Run static code analyzer
    result = analyze_code(request.code)

    # Generate rule-based improvement suggestions
    rule_suggestions = rule_based_ai(result)

    # Generate AI-based suggestions using Phi3 Mini
    llm_suggestions = phi3_mini_ai(request.code, result)

    # Calculate quality score
    score = calculate_score(result)

    # Return analysis result
    return {
        "analysis": result,
        "rule_based_suggestions": rule_suggestions,
        "llm_suggestions": llm_suggestions,
        "score": score
    }