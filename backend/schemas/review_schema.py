from pydantic import BaseModel


# Schema for the incoming request body
class CodeReviewRequest(BaseModel):
    code: str


# Schema for the API response
class CodeReviewResponse(BaseModel):
    status: str
    message: str