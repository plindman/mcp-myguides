
import os
import pytest
import pytest_asyncio
from fastmcp import Client
from pathlib import Path
from mcp_myguides.server.server import get_app, McpServer
from mcp_myguides.services.guide_repository import GuideRepository

@pytest_asyncio.fixture()
async def mcp_server(monkeypatch):
    # Monkeypatch AppSettings to point to test data via environment variable
    test_data_path = Path(__file__).parent.resolve() / "test_data"
    monkeypatch.setenv("MCP_MYGUIDES_GUIDES_ROOT_PATH", str(test_data_path))
    
    # Create the app in test environment
    return get_app()

@pytest_asyncio.fixture()
async def mcp_client(mcp_server):
    async with Client(mcp_server) as client_instance:
        yield client_instance

@pytest_asyncio.fixture()
async def guide_repository(monkeypatch):
    # Monkeypatch AppSettings to point to test data via environment variable
    test_data_path = Path(__file__).parent.resolve() / "test_data"
    monkeypatch.setenv("MCP_MYGUIDES_GUIDES_ROOT_PATH", str(test_data_path))
    return GuideRepository()
