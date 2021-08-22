from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PutScoring(BaseModel):
    certificate_id: Optional[int]


class Scoring(BaseModel):
    id: Optional[int]
    certificate_id: Optional[int]
    active: Optional[bool]
    approved: Optional[bool]
    denied: Optional[bool]
    score: Optional[float]
    score_violation_type: Optional[str]
    score_date: Optional[datetime]
    resolution_date: Optional[datetime]
