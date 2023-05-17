from datetime import date
from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        orm_mode = True


class ShowQuestion(TunedModel):
    question_id: int
    category_id: int
    question_text: str
    answer_text: str
    created_at: date

