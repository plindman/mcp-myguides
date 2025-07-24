import pytest
from pathlib import Path
from mcp_myguides.services.guide_repository import GuideRepository
from mcp_myguides.config.settings import get_settings

@pytest.mark.asyncio
async def test_guide_repository_paths(mcp_client):

    # Instantiate GuideRepository
    repo = GuideRepository()

    # Assert that the paths are correct
    test_data_path = Path(__file__).parent.resolve() / "test_data"
    test_yaml_path = test_data_path / "guides.yaml"
    assert repo.base_path.resolve() == test_data_path.resolve()
    assert repo.guides_yaml_path.resolve() == test_yaml_path.resolve()

    # Also check if the load method actually finds the file
    # This will print an error if not found, but the test will pass if no exception
    repo.load()
