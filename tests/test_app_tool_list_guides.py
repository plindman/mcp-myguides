import pytest
import json
from fastmcp import Client

@pytest.mark.asyncio
async def test_list_guides_tool(mcp_client: Client):
    """Tests the list_guides tool, including topic filtering."""
    response = await mcp_client.call_tool("list_guides")
    guides = json.loads(response.content[0].text)

    assert isinstance(guides, list)
    assert len(guides) == 1
    assert all(isinstance(g, dict) for g in guides)
    
    # Check for the known guide
    sample_guide = guides[0]
    assert sample_guide is not None
    assert sample_guide["name"] == "Sample Guide 1"

    # Test filtering by a known topic
    response_filtered = await mcp_client.call_tool("list_guides", arguments={"topic": "testing"})
    filtered_guides = json.loads(response_filtered.content[0].text)
    
    assert isinstance(filtered_guides, list)
    assert len(filtered_guides) == 1
    assert filtered_guides[0]["id"] == "sample-guide-1"
    assert "testing" in filtered_guides[0]["topics"]

