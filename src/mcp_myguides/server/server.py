from fastmcp import FastMCP
from functools import lru_cache
from ..config import get_settings
from .components_guides import register_guides_components
from ..utils.logging import setup_logging

@lru_cache
def get_app() -> FastMCP:
    setup_logging()
    settings = get_settings()
    app = FastMCP(
        name=settings.APP_NAME, 
        instructions=settings.APP_INSTRUCTIONS
    )
    register_guides_components(app)
    return app

class McpServer:
    def __init__(self):
        self.settings = get_settings()
        self.app = get_app()
    