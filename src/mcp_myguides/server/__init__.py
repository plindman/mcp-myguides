from fastmcp import FastMCP
from mcp_myguides.services.guide_repository import get_guide_repository_instance
from typing import TYPE_CHECKING

_app_instance: FastMCP | None = None

def get_app() -> FastMCP:
    global _app_instance
    if _app_instance is None:
        _app_instance = FastMCP()
        # Initialize GuideRepository and register components here
        guide_repository = get_guide_repository_instance()

        # Import modules here to ensure decorators register with the app instance
        from . import components_guides
        from . import tool_health

    return _app_instance

# This is needed for type checking, but not for runtime
if TYPE_CHECKING:
    app = get_app()
else:
    # This is a placeholder for runtime, will be set by get_app()
    app = None