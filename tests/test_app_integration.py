
import pytest
import json
from fastmcp import Client

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
async def test_get_guides_content_by_tags_tool(mcp_client: Client):
    """Tests getting combined guide content by a specific tag."""
    response = await mcp_client.call_tool("get_guides_content_by_tags", arguments={"tags": ["testing"]})
    content = response.content[0].text

    assert isinstance(content, str)
    assert "This is a sample guide for testing purposes." in content

@pytest.mark.asyncio
async def test_fetch_remote_guide(mocker, mcp_client: Client):
    """Tests fetching content from a remote guide URL."""
    mock_response = mocker.Mock()
    mock_response.text = "Content from Google Python Style Guide"
    mock_response.raise_for_status.return_value = None
    mocker.patch("httpx.AsyncClient.get", return_value=mock_response)

    response = await mcp_client.call_tool("get_guides_content_by_tags", arguments={"tags": ["style-guide"]})
    content = response.content[0].text

    assert isinstance(content, str)
    assert "Content from Google Python Style Guide" in content
