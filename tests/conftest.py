import pytest
import pytest_asyncio
from fastmcp import Client
from src.server import get_app

@pytest_asyncio.fixture
async def mcp_server():
    return get_app()

@pytest_asyncio.fixture
async def mcp_client(mcp_server):
    async with Client(mcp_server) as client_instance:
        yield client_instance