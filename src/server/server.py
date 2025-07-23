from fastmcp import FastMCP
from typing import Optional
from src.config.settings import get_settings

_app_instance: Optional[FastMCP] = None

def get_app() -> FastMCP:
    global _app_instance
    if _app_instance is None:
        settings = get_settings()
        _app_instance = FastMCP(name=settings.APP_NAME, instructions=settings.APP_INSTRUCTIONS)
    return _app_instance
