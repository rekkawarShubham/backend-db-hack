# app/models.py
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    name: str
    age: int
    gender: str
    caste: str
    city: str
    health_status: Optional[str]
    income: float
    employment_type: str

class Recommendation(BaseModel):
    scheme_id: int
    name: str
    category: str
    description: str