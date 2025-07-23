
import json
import pytest
from fastmcp import Client

@pytest.mark.asyncio
async def test_health_tool(mcp_client: Client):
    """Tests that the health check tool returns OK."""
    response = await mcp_client.call_tool("health")
    assert response.content[0].text == "OK"

@pytest.mark.asyncio
async def test_list_guides_tool(mcp_client: Client):
    """Tests the list_guides tool, including topic filtering."""
    # Test without filtering
    response = await mcp_client.call_tool("list_guides")
    guides = json.loads(response.content[0].text)

    assert isinstance(guides, list)
    assert len(guides) == 1  # We know there is only one guide in the test data
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

@pytest.mark.asyncio
async def test_guide_resource_access(mcp_client: Client):
    """Tests direct access to a guide resource using a known ID."""
    guide_id = "sample-guide-1"
    resource_path = f"mcp:///guides/{guide_id}"
    
    resource_content_list = await mcp_client.read_resource(resource_path)

    assert isinstance(resource_content_list, list)
    assert len(resource_content_list) == 1
    content = resource_content_list[0].text
    assert isinstance(content, str)
    assert "This is a sample guide for testing purposes." in content

@pytest.mark.asyncio
async def test_non_existent_guide_resource(mcp_client: Client):
    """Tests that accessing a non-existent guide returns empty content."""
    resource_path = "mcp:///guides/non-existent-guide-123"
    resource_content_list = await mcp_client.read_resource(resource_path)
    
    assert isinstance(resource_content_list, list)
    assert len(resource_content_list) == 1
    assert resource_content_list[0].text == ""

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
