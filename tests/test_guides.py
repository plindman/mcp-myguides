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

@pytest.mark.asyncio
async def test_load_all_guides_data_placeholder():
    # This test will be implemented later when load_all_guides_data is developed.
    assert True