import json
import pytest
import pytest_asyncio
from fastmcp import Client

@pytest.mark.asyncio
async def test_health_tool(mcp_client):
    response = await mcp_client.call_tool("health")
    assert response.content[0].text == "OK"

@pytest.mark.asyncio
async def test_list_guides_tool(mcp_client):
    response = await mcp_client.call_tool("list_guides")
    guides = json.loads(response.content[0].text) # Assuming the tool returns a list of GuideMetadata as JSON string

    assert isinstance(guides, list)
    assert len(guides) > 0 # Assuming there's at least one guide in guides.yaml
    assert all(isinstance(g, dict) for g in guides) # FastMCP serializes Pydantic models to dicts
    assert all("id" in g and "name" in g for g in guides)

    # Test filtering by topic (assuming 'test' is a topic in your sample guides)
    response_filtered = await mcp_client.call_tool("list_guides", arguments={"topic": "testing"})
    filtered_guides = json.loads(response_filtered.content[0].text)
    assert isinstance(filtered_guides, list)
    assert len(filtered_guides) > 0
    assert all("testing" in g.get("topics", []) for g in filtered_guides)

@pytest.mark.asyncio
async def test_guide_resource_access(mcp_client):
    # First, get a guide ID from the list_guides tool
    response = await mcp_client.call_tool("list_guides")
    guides = json.loads(response.content[0].text)

    if not guides:
        pytest.skip("No guides found to test resource access.")

    # Take the first guide's ID
    guide_id = guides[0]["id"]

    # Access the resource directly
    resource_path = f"mcp:///guides/{guide_id}"
    resource_content_list = await mcp_client.read_resource(resource_path)

    assert isinstance(resource_content_list, list)
    assert len(resource_content_list) > 0
    assert isinstance(resource_content_list[0].text, str) # Expecting raw text content
    assert len(resource_content_list[0].text) > 0 # Content should not be empty

@pytest.mark.asyncio
async def test_non_existent_guide_resource(mcp_client):
    resource_path = "mcp:///guides/non-existent-guide-123"
    resource_content_list = await mcp_client.read_resource(resource_path)
    assert isinstance(resource_content_list, list)
    assert len(resource_content_list) == 1 # Expecting one resource object
    assert resource_content_list[0].text == "" # Expecting empty text content

@pytest.mark.asyncio
async def test_get_guides_content_by_topic_tool(mcp_client):
    # Assuming 'test' is a topic in your sample guides
    response = await mcp_client.call_tool("get_guides_content_by_topic", arguments={"topic": "testing"})
    content = response.content[0].text

    assert isinstance(content, str)
    assert len(content) > 0
    # Further assertions can be made if you know specific content to expect
    # For example, check for a substring that should be present in combined content