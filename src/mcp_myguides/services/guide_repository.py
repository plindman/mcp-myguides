import yaml
from pathlib import Path
from typing import Dict, List, Optional
from pydantic import ValidationError
from functools import lru_cache
from mcp_myguides.core.models import GuideMetadata, Guide
from mcp_myguides.services.guide_loader import load_guide_content
from mcp_myguides.config import get_settings

@lru_cache
def get_guide_repository_instance() -> 'GuideRepository':
    return GuideRepository()

class GuideRepository:
    """
    Manages the collection of guides, loading their metadata from a YAML configuration
    and providing methods to access them and their content (lazily).
    """
    def __init__(self):
        settings = get_settings()
        self.guides_root_path = settings.GUIDES_ROOT_PATH
        self.guides: Dict[str, GuideMetadata] = {}
        self.content_cache: Dict[str, str] = {}

        self.load()

    def load(self):
        """
        Parses all guides.yaml files found recursively within GUIDES_ROOT_PATH
        and loads guide metadata into memory. Content is loaded lazily.
        """
        for guides_yaml_path in self.guides_root_path.rglob('guides.yaml'):
            try:
                with open(guides_yaml_path, 'r') as f:
                    config = yaml.safe_load(f)
                if config is None: # Handle empty YAML files
                    continue
            except FileNotFoundError:
                print(f"Warning: guides.yaml not found at {guides_yaml_path}")
                continue
            except yaml.YAMLError as e:
                print(f"Warning: Error parsing YAML file {guides_yaml_path}: {e}")
                continue

            for entry in config:
                try:
                    metadata = GuideMetadata(**entry)
                except ValidationError as e:
                    print(f"Warning: Skipping invalid guide entry in {guides_yaml_path}: {entry}. Error: {e}")
                    continue
                if metadata.id in self.guides:
                    print(f"Warning: Duplicate guide ID '{metadata.id}' found in {guides_yaml_path}. Skipping.")
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

        content = await load_guide_content(metadata.source, self.guides_root_path)
        self.content_cache[guide_id] = content
        return content

    def list_guides_metadata(self, tags: List[str] = None) -> List[GuideMetadata]:
        """
        Returns a list of guide metadata, optionally filtered by a list of tags.
        If multiple tags are provided, returns guides that have all of the tags.
        """
        guides_metadata = list(self.guides.values())
        if tags:
            return [
                guide for guide in guides_metadata if all(tag in guide.tags for tag in tags)
            ]
        return guides_metadata

    def list_tags(self) -> List[str]:
        """
        Returns a list of all unique tags from all guides.
        """
        all_tags = set()
        for guide in self.guides.values():
            all_tags.update(guide.tags)
        return sorted(list(all_tags))

    async def get_guides_content_by_tags(self, tags: List[str]) -> str:
        """
        Returns the concatenated content of all guides with the given tags, loading lazily.
        """
        filtered_guides_metadata = self.list_guides_metadata(tags=tags)
        contents = []
        for metadata in filtered_guides_metadata:
            content = await self.get_guide_content(metadata.id)
            if content:
                contents.append(content)
        return "\n---\n\n".join(contents)

    async def get_guide(self, guide_id: str) -> Optional[Guide]:
        """
        Retrieves a full guide object (metadata + content) by its ID.
        """
        metadata = self.get_guide_metadata(guide_id)
        if not metadata:
            return None
        content = await self.get_guide_content(guide_id)
        return Guide(metadata=metadata, content=content)