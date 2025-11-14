from sqlmodel import select
from .models import Question, Answer
from .database import get_session
from typing import List, Optional

def create_question(text: str) -> Question:
    with get_session() as session:
        q = Question(text=text)
        session.add(q)
        session.commit()
        session.refresh(q)
        return q

def list_questions() -> List[Question]:
    with get_session() as session:
        return session.exec(select(Question)).all()

def get_question_with_answers(qid: int) -> Optional[Question]:
    with get_session() as session:
        q = session.get(Question, qid)
        if not q:
            return None
        q.answers = session.exec(select(Answer).where(Answer.question_id == qid)).all()
        return q

def delete_question(qid: int) -> bool:
    with get_session() as session:
        q = session.get(Question, qid)
        if not q:
            return False
        # delete answers then question (cascade simulation)
        session.query(Answer).filter(Answer.question_id == qid).delete()
        session.delete(q)
        session.commit()
        return True

def create_answer(question_id: int, user_id: str, text: str) -> Optional[Answer]:
    with get_session() as session:
        q = session.get(Question, question_id)
        if not q:
            return None
        ans = Answer(question_id=question_id, user_id=user_id, text=text)
        session.add(ans)
        session.commit()
        session.refresh(ans)
        return ans

def get_answer(aid: int) -> Optional[Answer]:
    with get_session() as session:
        return session.get(Answer, aid)

def delete_answer(aid: int) -> bool:
    with get_session() as session:
        a = session.get(Answer, aid)
        if not a:
            return False
        session.delete(a)
        session.commit()
        return True
