import pytest
from mcp_myguides.server.server import McpServer

@pytest.mark.asyncio
async def test_app_common(mcp_server):

    assert mcp_server is not None

    server = McpServer()
    assert server.app is not None
    assert server.settings is not None

    settings = server.settings
    base_path = settings.GUIDES_BASE_PATH
    print(base_path)
    assert base_path is not None
    assert base_path.exists()