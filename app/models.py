from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Answer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question_id: int = Field(foreign_key="question.id", index=True)
    user_id: str
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # relationship back to question (optional)
    question: "Question" = Relationship(back_populates="answers")

class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    answers: List[Answer] = Relationship(back_populates="question")
