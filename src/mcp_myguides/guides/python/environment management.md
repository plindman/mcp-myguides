# uv for efficient project and environment management
Create a new project using `uv`. 
Assume `uv` is already installed. 
Run `uv init` in an empty directory to create a basic project with its pyproject.toml. If you're developing a reusable Python package, specifically use `uv init --lib`.
Use `uv sync` to refresh the project. 
These commands will automatically create a virtual environment (typically in a `.venv` directory in the project root) and install all dependencies specified in `pyproject.toml`.
* Manage project dependencies with `uv`. 
    * Add a new dependency: `uv add <package-name>`
    * Add a development-only dependency: `uv add --dev <package-name>`
    * Remove a dependency: `uv remove <package-name>`
    * Update all dependencies: `uv update`
* Do NOT add dependencies in advance. Always ask before adding new dependencies.
Only add dependencies you really need at the moment for the app. Remove unused dependencies when possible.
* Running Code. Use `uv run [project app command]`. Examples: `uv run fastapi dev main.py`, `uv run streamlit run app.py`.

### Dependency Categories and Pinning Strategy

**Production Dependencies:**
- Pin exact versions for critical infrastructure: fastapi==0.104.1
- Use compatible release for stable libraries: pydantic~=2.5.0 (allows 2.5.x)
- Avoid loose pins for security-sensitive packages: cryptography>=41.0.0,<42.0.0

**Development Dependencies:**
- Can be more flexible with versions: pytest>=7.0.0
- Pin exact versions for formatting/linting tools to ensure consistency: ruff==0.1.6
- Test runners can use compatible release: pytest~=7.4.0

**Handling Dependency Conflicts & Prevention Strategies**
- Use `uv tree` to visualize dependency relationships
- Regularly audit dependencies with `uv list --outdated`
- Pin problematic transitive dependencies when necessary
- Identify the conflict: `uv sync` will show conflicting requirements
- Analyze dependencies: Use `uv tree` to understand the dependency chain
