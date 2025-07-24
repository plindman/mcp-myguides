from fastmcp import FastMCP
from mcp_myguides.services.guide_repository import get_guide_repository_instance
from mcp_myguides.core.models import GuideMetadata
from typing import List

def register_guides_components(app: FastMCP) -> None:
    
    @app.tool
    async def list_guides(topic: str = None) -> List[GuideMetadata]:
        return get_guide_repository_instance().list_guides_metadata(topic=topic)

    @app.tool
    async def get_guides_content_by_topic(topic: str) -> str:
        return await get_guide_repository_instance().get_guides_content_by_topic(topic)

    @app.resource("mcp:///guides/{guide_id}")
    async def get_guide_resource(guide_id: str) -> str:
        return await get_guide_repository_instance().get_guide_content(guide_id)

    @app.resource("mcp:///guides/{guide_id}/metadata")
    async def get_guide_metadata(guide_id: str) -> GuideMetadata:
        return get_guide_repository_instance().get_guide_metadata(guide_id)

    @app.resource("mcp:///guides/{guide_id}/content")
    async def get_guide_content(guide_id: str) -> str:
        return await get_guide_repository_instance().get_guide_content(guide_id)
