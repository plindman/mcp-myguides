from fastmcp import FastMCP
from typing import Optional

# TODO: app settings from common pydantic settings for app
# name, instructions, ...

# Initialize the app instance as None
_app_instance: Optional[FastMCP] = None

def get_app() -> FastMCP:
    global _app_instance
    if _app_instance is None:
        _app_instance = FastMCP()
    return _app_instance
