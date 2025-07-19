### Development Plan: Personal MCP Server (Revised - with Central Metadata)

**Developer Reference:** All development should be guided by the official **[Model Context Protocol Server Quickstart](https://modelcontextprotocol.io/quickstart/server)**.

## Architecture Overview

This personal MCP server is designed to provide coding guidelines to AI agents via the Model Context Protocol. It leverages the `FastMCP` framework to expose these guidelines as discoverable and retrievable tools.

**Key Components:**

1.  **`guides.yaml` (Central Metadata Store):**
    *   A single YAML file located at the project root.
    *   Defines all available guides, including both local Markdown files and remote URLs.
    *   Each guide entry specifies its unique `id`, `name`, `description`, `topics` (for categorization), and `source` (local path or remote URL).
    *   This decouples metadata from content, allowing flexible management of diverse content sources.

2.  **`FastMCP` Server (`main.py`):**
    *   The core Python application built using `mcp.server.fastmcp`.
    *   On startup, it reads and parses `guides.yaml` to load all guide metadata and content into an in-memory data structure.
    *   Exposes three primary MCP tools for agents:
        *   **`list_guides()`:** Returns a list of all available guides, providing their `id`, `name`, `description`, and `topics`. This enables agents to discover relevant guidelines.
        *   **`get_guide_by_id(guide_id: str)`:** Retrieves the full Markdown content of a specific guide identified by its unique `id`.
        *   **`get_guides_by_topic(topic: str)`:** Returns a list of guides (metadata only) that are associated with a given `topic`, allowing agents to find guides related to a particular area (e.g., "python", "security").

3.  **Content Fetching Logic:**
    *   Integrated within the server's startup process.
    *   For local `source` paths, it reads the Markdown file directly from the filesystem.
    *   For remote `source` URLs, it uses `httpx` to fetch the content from the specified URL.

4.  **Caching (Future):**
    *   An in-memory cache will be implemented to store fetched guide content and metadata, reducing I/O operations and improving response times. Cache invalidation will be based on file modification times for local files and configurable durations for remote content.

**Interaction Flow:**

AI agents will interact with the server by first calling `list_guides()` to discover available guidelines. Based on their needs, they can then call `get_guide_by_id()` to retrieve specific content or `get_guides_by_topic()` to find relevant guides by category.

This plan outlines the steps to create a personal MCP server for your coding guidelines, following the `FastMCP` approach from the official documentation.

**Phase 1: Core Discovery and Retrieval Tools**

1.  **Project Setup & Fixed Tool Creation:**
    *   **Goal:** Create a runnable `FastMCP` server with `list_guides`, `get_guide_by_id`, and `get_guides_by_topic` tools that serve content from local Markdown files and remote URLs, with metadata defined in a central `guides.yaml`.
    *   **Steps:**
        1.  Ensure `guides/` directory exists and contains sample Markdown files.
        2.  **Create `guides.yaml`:** Create a `guides.yaml` file at the project root, defining all guides (local and remote) and their metadata as shown in the example above.
        3.  Modify `main.py` to:
            *   Initialize `FastMCP`.
            *   **Add `pyyaml` and `httpx` dependencies:** `pyyaml` for parsing `guides.yaml`, `httpx` for fetching remote content.
            *   Implement a `load_all_guides_data()` function that:
                *   Reads and parses `guides.yaml`.
                *   For each guide entry:
                    *   If `source` is a local file path, read the file content.
                    *   If `source` is a remote URL, fetch the content using `httpx`.
                    *   Store the `id`, `name`, `description`, `topics`, and the fetched `content`.
                *   This function will return a dictionary mapping `id`s to their full data (metadata + content).
            *   Define an `@app.tool()` decorated `list_guides()` function that calls `load_all_guides_data()` and returns a list of guide metadata (excluding `content`) for discovery. Each item in the list should include `id`, `name`, `description`, and `topics`.
            *   Define an `@app.tool()` decorated `get_guide_by_id(guide_id: str)` function that retrieves the full Markdown content of the specified guide by its `id` from the loaded data.
            *   Define an `@app.tool()` decorated `get_guides_by_topic(topic: str)` function that filters the loaded data by `topic` and returns a list of matching guides (e.g., their `id`, `name`, `description`, and `topics`).
            *   Ensure `app.run()` is called in the `if __name__ == "__main__":` block.
        4.  Run the server using `uvicorn` to confirm it works and the new tools are discoverable and callable.

**Phase 2: Advanced Features**

2.  **Caching Layer:**
    *   **Goal:** Implement a caching mechanism for guide content and metadata.
    *   **Steps:**
        1.  Modify `load_all_guides_data()` to cache the loaded data.
        2.  Implement cache invalidation based on file modification times (for local files), a configurable duration (for remote content), or a manual refresh trigger.

3.  **Manual Cache Refresh:**
    *   **Goal:** Allow for forcing a refresh of all content.
    *   **Steps:**
        1.  Expose a mechanism (e.g., a dedicated tool or command-line argument) to trigger a full cache refresh.

**Phase 3: Usability and Deployment**

4.  **CLI Integration and Deployment:**
    *   **Goal:** Make the server easily runnable from a Git repository using `uvx`.
    *   **Steps:**
        1.  Ensure `pyproject.toml` is correctly configured with all dependencies (`mcp`, `uvicorn`, `pyyaml`, `httpx`).
        2.  Update the `README.md` with clear instructions on how to run and use the server.
        3.  Push your code to a GitHub repository and test running it with `uvx run github:<your-username>/<your-repo>`.