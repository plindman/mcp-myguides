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

2.  **`FastMCP` Server (`main.py`):
    *   The core Python application built using `mcp.server.fastmcp`.
    *   Serves as the application entry point, responsible for initializing the `FastMCP` app and registering tools from various modules within the `src/` directory.
    *   On startup, it will orchestrate the loading and parsing of `guides.yaml` into an in-memory data structure.

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

1.  **DONE** Ensure the `guides/` directory exists and contains sample Markdown files.
2.  **DONE** Create a `guides.yaml` file at the project root, defining all guides (local and remote) and their metadata.
3.  **DONE** Add `pyyaml` ([PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)), `httpx` ([httpx Documentation](https://www.python-httpx.org/)), `pytest` ([pytest Documentation](https://docs.pytest.org/en/stable/)), and `pydantic` ([Pydantic Documentation](https://docs.pydantic.dev/latest/)) to `pyproject.toml` as dependencies.
4.  **DONE** Create a `tests/` directory at the project root.
5.  **DONE** Create `src/` directory and `src/__init__.py` to establish the `src` package.
6.  **DONE** Create `__init__.py` in the project root to make it a Python package.
7.  **DONE** Create `main.py` with a minimal `FastMCP` app instance and `app.run()` call.
8.  **DONE** Create `src/tools.py` and implement the `health()` tool within it.
9.  **DONE** Modify `main.py` to import and register the `health()` tool from `src.tools`.
10. **DONE** Create `tests/test_app.py` with a basic `pytest` test for the `health()` tool, using the `FastMCPClient` in-memory. This test will confirm the `FastMCP` app is running and testable.
11. **DONE** Verify Minimal App: Run `pytest` to confirm the core `FastMCP` setup and testing environment are working correctly.
12. **DONE** Configure `pyproject.toml` with a production start script (e.g., `start = "uvicorn main:app --host 0.0.0.0 --port 8000"`).
13. **DONE** Update `README.md` with clear instructions on how to run and use the server, including how to run tests.

## 4. Implementation Steps for the Developer

1.  **Implement Guide Data Loading and Validation:**
    *   Create `src/models.py` and define Pydantic models for guide metadata (e.g., `GuideMetadata` with fields for `id`, `name`, `description`, `topics`, `source`).
    *   Create `src/data_loader.py` and implement the `load_all_guides_data()` function within it. This function should:
        *   Read and parse `guides.yaml`.
        *   For each guide entry, validate it using the Pydantic model.
        *   If `source` is a local file path, read the file content.
        *   If `source` is a remote URL, fetch the content using `httpx`.
        *   Store the `id`, `name`, `description`, `topics`, and the fetched `content`.
        *   Return a dictionary mapping `id`s to their full data (metadata + content).
    *   Modify `main.py` to call `load_all_guides_data()` on startup and store the loaded data.
    *   Create `tests/test_data_loader.py` and write unit tests for `load_all_guides_data()` and Pydantic validation.
    *   **Run Tests:** Execute `pytest` to ensure data loading and validation function correctly.
    *   **Eager Commit:** Commit your changes after completing this step.

2.  **Implement Core Discovery and Retrieval Tools:**
    *   Implement `list_guides()`, `get_guide_by_id()`, and `get_guides_by_topic()` in `src/tools.py`.
    *   Ensure topic names are normalized to lowercase for comparison in `get_guides_by_topic()`.
    *   Include testing for the `health()` tool in `tests/test_tools.py`.
    *   Modify `main.py` to register these new tools from `src.tools`.
    *   Create `tests/test_tools.py` and write integration tests for these tools using the `FastMCPClient`.
    *   **Run Tests:** Execute `pytest` to ensure all implemented tools function correctly.
    *   **Eager Commit:** Commit your changes after completing this step.

3.  **Test Deployment:**
    *   Push your code to a GitHub repository and test running it with `uvx run github:<your-username>/<your-repo>`.
    *   **Eager Commit:** Commit your changes after completing this step.
