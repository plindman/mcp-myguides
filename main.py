from fastmcp import FastMCP

app = FastMCP("MCP server for my guides")

mock_guide = """
# Python Best Practices

- Follow PEP 8.
- Write docstrings for all public modules, functions, classes, and methods.
- Use a linter and code formatter.
"""

@app.tool()
async def python_best_practices() -> str:
    """Returns my personal guide for Python best practices."""
    return mock_guide

if __name__ == "__main__":
    app.run()