from fastapi import APIRouter
from pydantic import BaseModel
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai, llm_suggestions
from services.scoring_service import calculate_score

router = APIRouter(prefix="/review", tags=["Code Review"])

class CodeRequest(BaseModel):
    code: str

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
