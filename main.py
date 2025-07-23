""" Entry point for the MCP server. """
from src.server import get_app

app = get_app()

def start():
    app.run()

if __name__ == "__main__":
    start()
