from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_cursos():
    response = client.get("/api/v1/cursos")
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}

def test_post_curso():

    response = client.post("/api/v1/cursos", json={"titulo": "Hello World", "aulas": 12, "horas": 12, "autor_id": 1},)

    assert response.status_code == 201
