import pytest
import json
from fastmcp import Client

@pytest.mark.asyncio
async def test_list_guides_tool(mcp_client: Client):
    """Tests the list_guides tool, including tag filtering."""
    response = await mcp_client.call_tool("list_guides")
    guides = json.loads(response.content[0].text)

    assert isinstance(guides, list)
    assert len(guides) > 0  # Check for at least one guide
    assert all(isinstance(g, dict) for g in guides)
    
    # Find the sample guide
    sample_guide = next((g for g in guides if g["id"] == "sample-guide-1"), None)
    assert sample_guide is not None
    assert sample_guide["name"] == "Sample Guide 1"

    # Test filtering by a known tag
    response_filtered = await mcp_client.call_tool("list_guides", arguments={"tags": ["testing"]})
    filtered_guides = json.loads(response_filtered.content[0].text)
    
    assert isinstance(filtered_guides, list)
    assert len(filtered_guides) == 1
    assert filtered_guides[0]["id"] == "sample-guide-1"
    assert "testing" in filtered_guides[0]["tags"]

@pytest.mark.asyncio
async def test_list_tags_tool(mcp_client: Client):
    """Tests the list_tags tool."""
    response = await mcp_client.call_tool("list_tags")
    tags = json.loads(response.content[0].text)

    assert isinstance(tags, list)
    assert "general" in tags
    assert "testing" in tags
