### **Revised Plan (with Testing)**

1.  **Refine Data Loading (`src/data_loader.py`):**
    *   Create a `Guidebook` class to manage the collection of guides.
    *   This class will be responsible for parsing the `guides/guides.yaml` file and loading all guide data (metadata and content) into an in-memory collection.

2.  **Create a Discovery Tool (`src/tools.py`):**
    *   Implement a `list_guides(topic: str = None)` tool.
    *   This tool will **not** return the full guide content. Instead, it will return a list of guide *metadata* (ID, name, description, topics).
    *   If the optional `topic` argument is provided, the tool will filter the list to return only guides matching that topic.

3.  **Dynamically Create Guide Resources (`src/app.py`):**
    *   In the main application startup logic, after loading the guides via the `Guidebook`:
    *   Iterate through each loaded guide.
    *   For each guide, programmatically create and register a `TextResource`.
    *   The resource for each guide will be available at a unique, stable path: `/guides/{guide.id}`. This resource will serve the raw `content` of the guide.

4.  **Update Application Wiring (`src/app.py`):**
    *   Modify the `create_app` function to orchestrate the new logic:
        1.  Instantiate the `Guidebook`.
        2.  Load the guides using the `Guidebook`.
        3.  Register the `list_guides` tool, providing it access to the `Guidebook`.
        4.  Register the individual guide `TextResource`s.

5.  **Enable `uvx` Execution (`pyproject.toml` & `main.py`):**
    *   Add a `[project.scripts]` entry in `pyproject.toml` to define a console script entry point (e.g., `mcp-server = main:main`).
    *   Update `main.py` to have a `main()` function that initializes and runs the FastMCP application. This makes the project runnable as a package.

6.  **Implement Testing (`tests/`):**
    *   **Set up Pytest:** Ensure `pytest` is installed and configured for the project.
    *   **Test `Guidebook`:** Write unit tests for the `Guidebook` class in `tests/test_data_loader.py` to verify:
        *   Correct loading of guides from `guides.yaml`.
        *   Proper handling of local and remote sources (mocking `httpx` for remote calls).
        *   Accurate `get_guide` and `list_guides` functionality, including topic filtering.
    *   **Test FastMCP Integration:** Write integration tests in `tests/test_app.py` to verify:
        *   Correct registration of the `list_guides` tool.
        *   Successful dynamic registration and serving of guide resources (e.g., by making simulated HTTP requests to `/guides/{id}`).
        *   The `health` endpoint works as expected.

7.  **Documentation (`README.md`):**
    *   After the implementation is complete, create a `README.md` file.
    *   The `README.md` will include a "Development" section with instructions on how to:
        *   Set up a virtual environment using `uv venv`.
        *   Install dependencies using `uv sync`.
        *   Run the development server using `uv run`.
        *   **Run tests using `pytest`**.

8.  **Update `.gitignore`:**
    *   Ensure that the `.venv` directory created by `uv` is included in the `.gitignore` file.