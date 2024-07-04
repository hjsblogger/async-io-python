import pytest
import aiohttp
import sys
import os
# Add the project directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from fastapi.testclient import TestClient
from main import app  # Import the app from app/main.py

client = TestClient(app)

@pytest.mark.asyncio
async def test_fetch_builds():
    async with aiohttp.ClientSession() as session:
        response = client.get("/builds/")
        assert response.status_code == 200
        data = response.json()
        assert "dashboard_urls" in data
        assert isinstance(data["dashboard_urls"], list)

@pytest.mark.asyncio
async def test_fetch_sessions():
    async with aiohttp.ClientSession() as session:
        response = client.get("/sessions/")
        assert response.status_code == 200
        data = response.json()
        assert "session_names" in data
        assert isinstance(data["session_names"], list)

