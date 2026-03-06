from fastapi import APIRouter
from pydantic import BaseModel
from backend.schemas.review_schema import CodeReviewRequest, CodeReviewResponse
from backend.core.logging import logger

# Import service layer functions (implemented by Dev C)
from backend.services.code_analyzer import analyze_code
from backend.services.ai_engine import run_ai_engine
from backend.services.scoring_service import calculate_score
import time
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from backend.database.db import get_db
from backend.repositories.review_repo import create_review

# Create router for review-related APIs
router = APIRouter(prefix="/review", tags=["Code Review"])

class CodeRequest(BaseModel):
    code: str


# Secondary endpoint used for direct analysis testing

@router.post("/analyze")
def analyze_endpoint(request: CodeRequest,
                     db: Session = Depends(get_db)):

    analysis_result = analyze_code(request.code)

    ai_result = run_ai_engine(request.code, analysis_result)

    score = calculate_score(analysis_result)
    # save review to database
    review_data = {
        "code_snippet": request.code,
        "result": str(analysis_result),
        "score": score,
        "user_id": 1   # temporary user id for testing
    }

    create_review(db, review_data)

    return {
        "analysis": analysis_result,
        "rule_based_suggestions": ai_result["rule_based_suggestions"],
        "llm_suggestions": ai_result["llm_suggestions"],
        "rule_based_time_in_sec": ai_result["rule_based_time_in_sec"],
        "llm_time_in_sec": ai_result["llm_time_in_sec"],
        "total_time_in_sec": ai_result["total_time_in_sec"],
        "timestamp": ai_result["timestamp"],
        "score": score
    }