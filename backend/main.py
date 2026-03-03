from fastapi import FastAPI
from config import get_settings
from pydantic import BaseModel
from services.code_analyzer import analyze_code
from services.ai_engine import rule_based_ai

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)
class CodeRequest(BaseModel):
    code: str

@app.post("/analyze")
def analyze_endpoint(request: CodeRequest):
    result = analyze_code(request.code)
    suggestions = rule_based_ai(result)
    return {"analysis": result, "suggestions": suggestions}

#@app.get("/health")
#async def health_check():
 #   return {
  #      "status": "healthy",
   #     "app": settings.app_name,
    #    "version": settings.app_version
    #}