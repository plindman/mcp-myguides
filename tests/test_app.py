import pytest
from fastmcp import FastMCP, Client
from main import app
import pytest_asyncio

@pytest_asyncio.fixture
async def client():
    async with Client(app) as client_instance:
        yield client_instance

@pytest.mark.asyncio
async def test_health_tool(client):
    response = await client.call_tool("health")
    assert response.content[0].text == "OK"
