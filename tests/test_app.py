import pytest

from fastapi.testclient import TestClient
from sa.app import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_empty_input(client):
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422

    body = response.json()
    assert "Text cannot be empty" in body["detail"][0]["msg"]
