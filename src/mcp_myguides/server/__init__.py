from .server import get_app
from .components_guides import app as components_guides
from .tool_health import app as tool_health

mcp = get_app()

__all__ = ["mcp", "get_app"]
