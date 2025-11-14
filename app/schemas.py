from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional, List

NonEmptyStr = constr(strip_whitespace=True, min_length=1)

class QuestionCreate(BaseModel):
    text: NonEmptyStr

class QuestionRead(BaseModel):
    id: int
    text: str
    created_at: datetime

class AnswerCreate(BaseModel):
    user_id: str
    text: NonEmptyStr

class AnswerRead(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

class QuestionWithAnswers(QuestionRead):
    answers: List[AnswerRead] = []
