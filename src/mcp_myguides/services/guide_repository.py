import yaml
from pathlib import Path
from typing import Dict, List, Optional
from mcp_myguides.core.models import GuideMetadata, Guide
from pydantic import ValidationError
from mcp_myguides.services.guide_loader import load_guide_content
from mcp_myguides.config.settings import get_settings
import importlib.resources
import mcp_myguides

_guide_repository_instance: Optional['GuideRepository'] = None

def get_guide_repository_instance() -> 'GuideRepository':
    global _guide_repository_instance
    if _guide_repository_instance is None:
        _guide_repository_instance = GuideRepository()
        _guide_repository_instance.load()
    return _guide_repository_instance

class GuideRepository:
    """
    Manages the collection of guides, loading their metadata from a YAML configuration
    and providing methods to access them and their content (lazily).
    """
    def __init__(self):
        settings = get_settings()
        
        # Determine if running from installed package or development environment
        # This is a heuristic: if the guides_yaml_path from settings is a file,
        # assume development/test. Otherwise, try to load from package resources.
        if settings.guides_yaml_path.is_file():
            self.guides_yaml_path = settings.guides_yaml_path
            self.base_path = settings.GUIDES_BASE_PATH
        else:
            # Assume running from an installed package, load from resources
            self.guides_yaml_path = importlib.resources.files(mcp_myguides) / "guides" / settings.GUIDES_YAML_FILENAME
            self.base_path = importlib.resources.files(mcp_myguides) / "guides"

        self.guides: Dict[str, GuideMetadata] = {}
        self.content_cache: Dict[str, str] = {}

    def load(self):
        """
        Parses the guides.yaml file and loads only guide metadata into memory.
        Content is loaded lazily.
        """
        # Ensure the file exists before trying to open it
        if not self.guides_yaml_path.is_file():
            print(f"Error: guides.yaml not found at {self.guides_yaml_path}")
            return

        with open(self.guides_yaml_path, 'r') as f:
            config = yaml.safe_load(f)

        for entry in config:
            try:
                metadata = GuideMetadata(**entry)
            except ValidationError as e:
                print(f"Warning: Skipping invalid guide entry: {entry}. Error: {e}")
                continue
            self.guides[metadata.id] = metadata

    def get_guide_metadata(self, guide_id: str) -> Optional[GuideMetadata]:
        """
        Retrieves a single guide's metadata by its ID.
        """
        return self.guides.get(guide_id)

    async def get_guide_content(self, guide_id: str) -> str:
        """
        Retrieves the content of a single guide by its ID, loading it lazily if not cached.
        """
        if guide_id in self.content_cache:
            return self.content_cache[guide_id]

        metadata = self.get_guide_metadata(guide_id)
        if not metadata:
            return ""

        content = await load_guide_content(metadata.source, self.base_path)
        self.content_cache[guide_id] = content
        return content

    def list_guides_metadata(self, topic: str = None) -> List[GuideMetadata]:
        """
        Returns a list of guide metadata, optionally filtered by topic.
        """
        guides_metadata = list(self.guides.values())
        if topic:
            return [
                guide for guide in guides_metadata if topic in guide.topics
            ]
        return guides_metadata

    async def get_guides_content_by_topic(self, topic: str) -> str:
        """
        Returns the concatenated content of all guides with the given topic, loading lazily.
        """
        filtered_guides_metadata = self.list_guides_metadata(topic=topic)
        contents = []
        for metadata in filtered_guides_metadata:
            content = await self.get_guide_content(metadata.id)
            if content:
                contents.append(content)
        return "\n\n---\n\n".join(contents)