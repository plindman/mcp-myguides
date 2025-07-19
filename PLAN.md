### Development Plan: Personal MCP Server (MVP - with Central Metadata and Testing)

**Developer Reference:** All development should be guided by the official **[Model Context Protocol Server Quickstart](https://modelcontextprotocol.io/quickstart/server)**.

## 1. Intent

To develop a Minimum Viable Product (MVP) of a personal Model Context Protocol (MCP) server that provides coding guidelines to AI agents. This server will leverage the `FastMCP` framework to expose these guidelines as discoverable and retrievable tools, with all guide metadata managed centrally in a `guides.yaml` file. The development process will include robust testing using `pytest` and the in-memory `FastMCP` client.

## 2. Architecture

This personal MCP server is designed to provide coding guidelines to AI agents via the Model Context Protocol. It leverages the `FastMCP` framework to expose these guidelines as discoverable and retrievable tools.

**Key Components:**

1.  **`guides.yaml` (Central Metadata Store):**
    *   A single YAML file located at the project root.
    *   Defines all available guides, including both local Markdown files and remote URLs.
    *   Each guide entry specifies its unique `id`, `name`, `description`, `topics` (for categorization), and `source` (local path or remote URL).
    *   This decouples metadata from content, allowing flexible management of diverse content sources.

2.  **`FastMCP` Server (`main.py`):
    *   The core Python application built using `mcp.server.fastmcp`.
    *   On startup, it reads and parses `guides.yaml` to load all guide metadata and content into an in-memory data structure.
    *   Exposes three primary MCP tools for agents:
        *   **`list_guides()`:** Returns a list of all available guides, providing their `id`, `name`, `description`, and `topics`. This enables agents to discover relevant guidelines.
        *   **`get_guide_by_id(guide_id: str)`:** Retrieves the full Markdown content of a specific guide identified by its unique `id`.
        *   **`get_guides_by_topic(topic: str)`:** Returns a list of guides (metadata only) that are associated with a given `topic`, allowing agents to find guides related to a particular area (e.g., "python", "security").
        *   **`health()`:** A simple tool to confirm the server is running and responsive.

3.  **Content Fetching Logic:**
    *   Integrated within the server's startup process.
    *   For local `source` paths, it reads the Markdown file directly from the filesystem.
    *   For remote `source` URLs, it uses `httpx` to fetch the content from the specified URL.

4.  **Metadata Validation (Pydantic):**
    *   Pydantic models will be used to validate the structure and data types of entries in `guides.yaml`, ensuring data integrity and early error detection.

5.  **Topic Normalization:**
    *   Topic names will be normalized (e.g., converted to lowercase) to ensure consistent and reliable filtering.

6.  **Testing Framework (`pytest` and `FastMCP` Client):**
    *   Unit tests for data loading and parsing logic.
    *   Integration tests using `pytest` and the `FastMCP` client to interact with the server instance in-memory, verifying tool functionality.

**Interaction Flow:**

AI agents will interact with the server by first calling `list_guides()` to discover available guidelines. Based on their needs, they can then call `get_guide_by_id()` to retrieve specific content or `get_guides_by_topic()` to find relevant guides by category. They can also use the `health()` tool to check server status.

## 3. Scaffolding the Project Environment

1.  Ensure the `guides/` directory exists and contains sample Markdown files.
2.  Create a `guides.yaml` file at the project root, defining all guides (local and remote) and their metadata.
3.  Add `pyyaml` ([PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)), `httpx` ([httpx Documentation](https://www.python-httpx.org/)), `pytest` ([pytest Documentation](https://docs.pytest.org/en/stable/)), and `pydantic` ([Pydantic Documentation](https://docs.pydantic.dev/latest/)) to `pyproject.toml` as dependencies.
4.  Create a `tests/` directory at the project root.
5.  Configure `pyproject.toml` with a production start script (e.g., `start = "uvicorn main:app --host 0.0.0.0 --port 8000"`).
6.  Update `README.md` with clear instructions on how to run and use the server, including how to run tests.

## 4. Implementation Steps for the Developer

1.  **Set up Testing Environment and Initial Tests:**
    *   Create `tests/test_guides.py`.
    *   Write basic unit tests for the `load_all_guides_data()` function (even if it's just a placeholder for now).
    *   Write initial integration tests using `pytest` and the `FastMCP` client, passing the `FastMCP` app instance to the client for in-memory testing. Refer to [FastMCP Testing Patterns](https://gofastmcp.com/patterns/testing) for examples.
    *   **Run Tests:** Execute `pytest` to confirm the test setup is working.
    *   **Eager Commit:** Commit your changes after completing this step.

2.  **Implement Core Discovery and Retrieval Tools and Metadata Validation:**
    *   Modify `main.py` to initialize `FastMCP`.
    *   Define Pydantic models for guide metadata (e.g., `GuideMetadata` with fields for `id`, `name`, `description`, `topics`, `source`).
    *   Implement the `load_all_guides_data()` function that:
        *   Reads and parses `guides.yaml`.
        *   For each guide entry, validate it using the Pydantic model.
        *   If `source` is a local file path, read the file content.
        *   If `source` is a remote URL, fetch the content using `httpx`.
        *   Store the `id`, `name`, `description`, `topics`, and the fetched `content`.
        *   Return a dictionary mapping `id`s to their full data (metadata + content).
    *   Define an `@app.tool()` decorated `list_guides()` function that calls `load_all_guides_data()` and returns a list of guide metadata (excluding `content`) for discovery. Each item in the list should include `id`, `name`, `description`, and `topics`.
    *   Define an `@app.tool()` decorated `get_guide_by_id(guide_id: str)` function that retrieves the full Markdown content of the specified guide by its `id` from the loaded data.
    *   Define an `@app.tool()` decorated `get_guides_by_topic(topic: str)` function that filters the loaded data by `topic` (ensuring topic names are normalized to lowercase for comparison) and returns a list of matching guides (e.g., their `id`, `name`, `description`, and `topics`).
    *   Define an `@app.tool()` decorated `health()` function that returns a fixed status string (e.g., "OK").
    *   Ensure `app.run()` is called in the `if __name__ == "__main":` block.
    *   **Run Tests:** Execute `pytest` to ensure all implemented tools function correctly, including tests for metadata validation and the new `health` tool.
    *   **Eager Commit:** Commit your changes after completing this step.

3.  **Test Deployment:**
    *   Push your code to a GitHub repository and test running it with `uvx run github:<your-username>/<your-repo>`.
    *   **Eager Commit:** Commit your changes after completing this step.