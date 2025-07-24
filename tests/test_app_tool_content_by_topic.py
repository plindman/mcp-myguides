import pytest
import json
from fastmcp import Client

@pytest.mark.asyncio
async def test_get_guides_content_by_topic_tool(mcp_client: Client):
    """Tests getting combined guide content by a specific topic."""
    response = await mcp_client.call_tool("get_guides_content_by_topic", arguments={"topic": "testing"})
    content = response.content[0].text

    assert isinstance(content, str)
    assert "This is a sample guide for testing purposes." in content

@pytest.mark.asyncio
async def test_get_guides_content_by_non_existent_topic(mcp_client: Client):
    """Tests that getting content for a non-existent topic returns an empty string."""
    response = await mcp_client.call_tool("get_guides_content_by_topic", arguments={"topic": "non-existent-topic-xyz"})
    content = response.content[0].text

    assert isinstance(content, str)
    assert content == ""
