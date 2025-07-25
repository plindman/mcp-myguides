## Source Code Standards

We maintain high standards for code quality to ensure maintainability, reliability, and ease of collaboration.

### Coding Style

- Follow consistent Python style and structure for readable, maintainable code.
- Adhere to PEP 8 for naming, formatting, and layout
- Use ruff to automatically enforce style
- All new code must include type hints
- Avoid overly clever constructs – optimize for clarity

### Source Documentation

- Use Google-style docstrings for public functions, classes, and modules
- Use inline comments to explain why, not what
- For simple functions, type hints may be sufficient without full docstrings

* **Docstrings:** All functions, classes, and modules should have clear, concise docstrings following the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).
* **Inline Comments:** Use comments sparingly to explain *why* complex logic is implemented, not *what* it does.
 
**Docstring Requirements:**
- **Public APIs**: Always require comprehensive docstrings (classes, public methods, functions)
- **Private/Internal**: Brief docstrings for complex logic only
- **Simple utilities**: Type hints sufficient, docstring optional

**Format Examples:**
``` python
# Required - Public API
def process_user_data(data: dict[str, Any]) -> UserModel:
    """Process raw user data into validated model.
    
    Args:
        data: Raw user data from external source
        
    Returns:
        Validated user model instance
        
    Raises:
        ValidationError: If data fails validation
    """

# Optional - Simple utility  
def normalize_email(email: str) -> str:
    """Convert email to lowercase and strip whitespace."""
    return email.lower().strip()

# Not required - obvious function
def get_user_id(user: User) -> int:
    return user.id
```

### Quality Checks

- `ruff` is our linter and formatter, enforcing code style and catching common issues quickly.
- `mypy` supports robust type-checking and type annotation, helping us maintain code clarity and correctness. 
- `bandit`: For identifying common security vulnerabilities, Bandit helps us maintain a secure codebase.

Together, these tools help us maintain high code quality and follow best practices efficiently.

If any required tools (`ruff`, `pytest`, `mypy`, etc.) are missing from your local environment, install them as **development dependencies** using:
```bash
uv add --dev pytest ruff ty bandit
```

Do not add these tools to the production dependencies.

### Code Formatting and Linting using ruff 

*   `ruff` is our linter and formatter, enforcing code style and catching common issues quickly.
*   You can run `ruff` manually with:
    ```bash
    uv run ruff check --fix .   # Automatically fixes linting issues
    uv run ruff format .        # Formats code according to Black-like style
    ```

### Type Hinting & Static Analysis

*   **All new code must include type hints.**
*   Existing code should be updated with type hints as part of refactoring or feature work.
*   You can run mypy manually with:
    ```bash
    uv run mypy src/
    ```
