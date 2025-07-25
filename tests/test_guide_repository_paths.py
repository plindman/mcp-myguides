import pytest
from pathlib import Path
from mcp_myguides.services.guide_repository import GuideRepository
from mcp_myguides.config.settings import get_settings

@pytest.mark.asyncio
async def test_guide_repository_paths(guide_repository):

    # Assert that a guide from the test_data directory is loaded
    guide_metadata = guide_repository.get_guide_metadata("sample-guide-1")
    assert guide_metadata is not None
    assert guide_metadata.id == "sample-guide-1"

    # Assert that the content can be loaded
    content = await guide_repository.get_guide_content("sample-guide-1")
    assert "This is a sample guide for testing purposes." in content
