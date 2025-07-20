from fastmcp import FastMCP
from src.tools import register_tools

app = FastMCP()
register_tools(app)

if __name__ == "__main__":
    app.run()