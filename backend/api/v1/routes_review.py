from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai
from services.scoring_service import calculate_score

router = APIRouter(prefix="/review", tags=["Code Review"])

class CodeRequest(BaseModel):
    code: str

@router.post("/analyze")
def analyze_endpoint(request: CodeRequest):
    result = analyze_code(request.code)
    suggestions = rule_based_ai(result)
    score = calculate_score(result)
    return {
        "analysis": result,
        "suggestions": suggestions,
        "score": score
    }