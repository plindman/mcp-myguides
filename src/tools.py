from fastmcp import FastMCP

def register_tools(app: FastMCP):
    @app.tool()
    def health():
        return "OK"
