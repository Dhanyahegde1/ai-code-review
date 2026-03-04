from pydantic import BaseModel


class CodeReviewRequest(BaseModel):
    code: str


class CodeReviewResponse(BaseModel):
    status: str
    message: str