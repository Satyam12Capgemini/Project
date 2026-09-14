from pydantic import BaseModel
from typing import List


class ReviewResult(BaseModel):
    reviewType: str
    agent: str
    riskLevel: str
    findings: list
    recommendations: list
    nextActions: list
    rawResponse: str