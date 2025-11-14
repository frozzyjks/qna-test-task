from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_question_and_answer():
    # create question
    q_resp = client.post("/questions/", json={"text": "Как дела?"})
    assert q_resp.status_code == 201
    q = q_resp.json()
    qid = q["id"]

    # create answer
    a_resp = client.post(f"/questions/{qid}/answers/", json={"user_id": "u1", "text": "Хорошо"})
    assert a_resp.status_code == 201
    a = a_resp.json()
    assert a["question_id"] == qid

    # get question with answers
    get_q = client.get(f"/questions/{qid}")
    assert get_q.status_code == 200
    body = get_q.json()
    assert len(body.get("answers", [])) >= 1

    # delete question (cascade)
    del_q = client.delete(f"/questions/{qid}")
    assert del_q.status_code == 204
