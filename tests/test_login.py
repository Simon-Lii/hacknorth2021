import pytest
from backend.app import app

TESTING_NAME = "84f4de289e564bef952b05839cd9b99c"
TESTING_PASSWORD = "ab50334727754af8b33082fc1a023908"


def test_create_delete_user():
    with app.test_client() as client:
        resp = client.post("/api/create_user", data={"username": TESTING_NAME, "password": TESTING_PASSWORD})
        client.post("/api/delete_user", data={"username": "test6", "password": "test3"})
        assert resp.status_code == 200
        assert resp.json["status"] == "success"


pytest.main()