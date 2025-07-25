import pytest
from fastmcp import Client

@pytest.mark.asyncio
async def test_get_guides_content_by_tags(mcp_client: Client):
    """Tests the get_guides_content_by_tags tool."""
    response = await mcp_client.call_tool("get_guides_content_by_tags", arguments={"tags": ["testing"]})
    content = response.content[0].text

    assert "This is a sample guide for testing purposes." in content