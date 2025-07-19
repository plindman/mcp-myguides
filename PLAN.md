### Development Plan: Personal MCP Server (Revised)

This plan outlines the steps to create a personal MCP server for your coding guidelines, following the `FastMCP` approach from the official documentation.

**Phase 1: Dynamic Content from Local Files**

1.  **Project Setup & Dynamic Tool Creation:**
    *   **Goal:** Create a runnable `FastMCP` server that dynamically creates tools from local Markdown files.
    *   **Steps:**
        1.  Create a `guides/` directory.
        2.  Add a sample guide file to the directory (e.g., `python-style-guide.md`).
        3.  Modify `main.py` to:
            *   Scan the `guides/` directory for `.md` files on startup.
            *   For each file, dynamically create and register a tool with the `FastMCP` application.
            *   The tool's name will be derived from the filename (e.g., `python_style_guide`).
            *   The tool's description will be the first line of the Markdown file.
            *   The tool's function will be to return the content of the file.
        4.  Run the server using `uvicorn` to confirm it works.

**Phase 2: Advanced Features**

2.  **Caching Layer:**
    *   **Goal:** Implement a caching mechanism to avoid re-reading files on every request.
    *   **Steps:**
        1.  Add an in-memory cache to store the guide content.
        2.  When a tool is called, check the cache first. If the content isn't there, read the file, store it in the cache, and then return it.
        3.  Add a timestamp and a configurable duration to the cache to allow for periodic refreshes.

3.  **Remote Content from URLs:**
    *   **Goal:** Fetch guides from a list of URLs.
    *   **Steps:**
        1.  Add a configuration mechanism (e.g., a `config.py` file or a simple text file) to specify a list of URLs to Markdown files.
        2.  Use a library like `httpx` to fetch the content from these URLs.
        3.  Extend the dynamic tool creation logic to create tools from the fetched content.
        4.  The caching mechanism will also apply to these remote guides.

4.  **Manual Cache Refresh:**
    *   **Goal:** Allow for forcing a refresh of all content.
    *   **Steps:**
        1.  Expose a mechanism to trigger a cache refresh (e.g., a command-line argument or a special tool).
        2.  When triggered, clear the cache and re-fetch all local and remote guides.

**Phase 3: Usability and Deployment**

5.  **CLI Integration and Deployment:**
    *   **Goal:** Make the server easily runnable from a Git repository using `uvx`.
    *   **Steps:**
        1.  Ensure `pyproject.toml` is correctly configured with all dependencies (`mcp`, `uvicorn`, `httpx`).
        2.  Update the `README.md` with clear instructions on how to run and use the server.
        3.  Push your code to a GitHub repository and test running it with `uvx run github:<your-username>/<your-repo>`.
