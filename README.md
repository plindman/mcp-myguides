# Personal MCP Guides Server

This project implements a personal Model Context Protocol (MCP) server to provide coding guidelines to AI agents. It uses `FastMCP` to expose discoverable and retrievable tools, with guide metadata managed centrally in `guides.yaml`.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd mcp-myguides
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management. Ensure you have `uv` installed.
    ```bash
    uv sync
    ```

## Running the Server

To start the FastMCP server:

```bash
uv run start
```

The server will be accessible at `http://0.0.0.0:8000` (or the port you configure).

## Adding New Guides

1.  **Create your Markdown guide file:**
    Place your Markdown files (e.g., `my_new_guide.md`) in the `guides/` directory.

2.  **Update `guides.yaml`:**
    Open `guides.yaml` at the project root and add an entry for your new guide. Ensure you provide a unique `id`, `name`, `description`, relevant `topics`, and the `source` path to your Markdown file.

    Example `guides.yaml` entry:
    ```yaml
    - id: my-new-guide
      name: My New Coding Guide
      description: Guidelines for writing clean code.
      topics: [coding, best-practices, python]
      source: guides/my_new_guide.md
    ```

## Running Tests

This project uses `pytest` for testing. To run the tests:

```bash
uv run pytest
```

## Project Structure

-   `main.py`: The main FastMCP server application.
-   `guides.yaml`: Central metadata store for all guides.
-   `guides/`: Directory containing Markdown files for local guides.
-   `tests/`: Directory for all test files.
-   `pyproject.toml`: Project configuration and dependencies.
