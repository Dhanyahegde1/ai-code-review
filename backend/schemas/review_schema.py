from pydantic import BaseModel
from typing import List

# Schema for the incoming request body
class CodeReviewRequest(BaseModel):
    code: str


# Schema for the API response
class CodeReviewResponse(BaseModel):
    status: str
    message: str
    timestamp: str
    rule_based_time: float
    llm_time: float
    total_time: float

    rule_based_suggestions: List[str]
    llm_suggestions: str