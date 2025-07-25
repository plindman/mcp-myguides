import pytest
from mcp_myguides.server.server import McpServer

@pytest.mark.asyncio
async def test_app_common(mcp_server):

    assert mcp_server is not None

    server = McpServer()
    assert server.app is not None
    assert server.settings is not None

    settings = server.settings
    root_path = settings.GUIDES_ROOT_PATH
    print(root_path)
    assert root_path is not None
    assert root_path.exists()