from fastapi import FastAPI
from config import get_settings
from pydantic import BaseModel
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai
from services.scoring_service import calculate_score  # import your scoring function
from config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)
class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
def analyze_endpoint(request: CodeRequest):
    # 1. analyze the code
    result = analyze_code(request.code)
    # 2. generate the suggestions
    suggestions = rule_based_ai(result)
    # 3. calculating the score
    score = calculate_score(result)

    # return everything
    return {"analysis": result, 
            "suggestions": suggestions,
            "score":score}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }