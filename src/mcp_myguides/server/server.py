from fastmcp import FastMCP
from functools import lru_cache
from ..config import get_settings
from .tool_health import register_health_tool
from .components_guides import register_guides_components

@lru_cache
def get_app() -> FastMCP:
    settings = get_settings()
    app = FastMCP(
        name=settings.APP_NAME, 
        instructions=settings.APP_INSTRUCTIONS
    )
    register_health_tool(app)
    register_guides_components(app)
    return app

class McpServer:
    def __init__(self):
        self.settings = get_settings()
        self.app = get_app()
    