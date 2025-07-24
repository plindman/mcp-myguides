import pytest
import json
from fastmcp import Client

@pytest.mark.asyncio
async def test_health_tool(mcp_client: Client):
    """Tests that the health check tool returns OK."""
    response = await mcp_client.call_tool("health")
    assert response.content[0].text == "OK"
