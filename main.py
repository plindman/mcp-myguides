""" Entry point for the MCP server. """
from src.server import get_app

app = get_app()

if __name__ == "__main__":
    app.run()
