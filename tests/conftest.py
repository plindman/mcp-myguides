import pytest
import pytest_asyncio
from fastmcp import Client
from mcp_myguides.server import get_app
from pathlib import Path

@pytest_asyncio.fixture
async def mcp_server():
    return get_app()

@pytest_asyncio.fixture
async def mcp_client(mcp_server):
    async with Client(mcp_server) as client_instance:
        yield client_instance

@pytest.fixture(scope="function", autouse=True)
def setup_test_environment(monkeypatch):
    """
    This fixture runs for each test, setting the environment variable
    to point to our test data.
    """
    test_data_path = Path(__file__).parent / "test_data"
    monkeypatch.setenv("GUIDES_BASE_PATH", str(test_data_path))