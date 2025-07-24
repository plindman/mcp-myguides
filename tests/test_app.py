import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_app_common(mcp_client):
    # The mcp_client fixture already handles the client's context.
    # We can interact with it directly.

    # Basic server interaction
    await mcp_client.ping()
    
    # List available operations
    tools = await mcp_client.list_tools()
    resources = await mcp_client.list_resources()

    # assert tools
    # assert resources

    # prompts = await mcp_client.list_prompts()
    # assert prompts

