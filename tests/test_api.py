import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add API path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'apps', 'api'))

from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "MUSE"

def test_health():
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_event_types():
    response = client.get("/api/v1/events/types")
    assert response.status_code == 200
    assert "USER_LIKED_POST" in response.json()["event_types"]

def test_create_event_invalid_type():
    response = client.post("/api/v1/events/", json={
        "user_id": 1,
        "event_type": "INVALID_EVENT",
        "data": {}
    })
    assert response.status_code == 400
