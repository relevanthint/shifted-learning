from pydantic import BaseModel
from typing import Optional


class BaseWording(BaseModel):
    id: Optional[int]
    baseWording: str
    theme: str
    tone: str
    length: str
    learningObjective: str
    use_gpt4: bool