from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_cursos():
    response = client.get("/api/v1/cursos")
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}