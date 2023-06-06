from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_uploading_data_eng():
    response = client.post(
        "/upload",
        json={
            "text": "Could you be humble?"
        })
    assert response.status_code == 200
    assert "token" in response.json()


def test_uploading_data_ru():
    response = client.post(
        "/upload",
        json={
            "text": "Можешь помолчать пожалуйста?",
            "lang": "ru"
        })
    assert response.status_code == 200
    assert "token" in response.json()


def test_result_data():
    response = client.get(
        "/result",
        params={
            "token": "5ddb122b073837d174fc15cb7dce3053dbad0f81"
        })
    assert response.status_code == 200
    assert response.json()["result"]["better_result"]["score"] != 0


