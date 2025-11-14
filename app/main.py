from fastapi import FastAPI, HTTPException, status
from . import crud, database
from .schemas import (
    QuestionCreate, QuestionRead, QuestionWithAnswers,
    AnswerCreate, AnswerRead
)

app = FastAPI(title="QnA API")

@app.on_event("startup")
def on_startup():
    database.init_db()

@app.get("/questions/", response_model=list[QuestionRead])
def list_questions():
    qs = crud.list_questions()
    return qs

@app.post("/questions/", response_model=QuestionRead, status_code=status.HTTP_201_CREATED)
def create_question(q: QuestionCreate):
    created = crud.create_question(q.text)
    return created

@app.get("/questions/{question_id}", response_model=QuestionWithAnswers)
def get_question(question_id: int):
    q = crud.get_question_with_answers(question_id)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q

@app.delete("/questions/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int):
    ok = crud.delete_question(question_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Question not found")
    return

@app.post("/questions/{question_id}/answers/", response_model=AnswerRead, status_code=status.HTTP_201_CREATED)
def add_answer(question_id: int, payload: AnswerCreate):
    ans = crud.create_answer(question_id, payload.user_id, payload.text)
    if not ans:
        raise HTTPException(status_code=404, detail="Question not found")
    return ans

@app.get("/answers/{answer_id}", response_model=AnswerRead)
def get_answer(answer_id: int):
    a = crud.get_answer(answer_id)
    if not a:
        raise HTTPException(status_code=404, detail="Answer not found")
    return a

@app.delete("/answers/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int):
    ok = crud.delete_answer(answer_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Answer not found")
    return
