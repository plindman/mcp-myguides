""" Health check tool """
from fastmcp import FastMCP

def register_health_tool(app: FastMCP) -> None:

    @app.tool
    async def health() -> str:
        return "OK"
