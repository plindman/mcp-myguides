# Preferred Libraries

Prefer the use of the following preferred libraries to ensure high quality, maintainability, and efficient development.

## Application

* **`fastapi`**: For rapidly building high-performance asynchronous APIs. To ensure all standard dependencies are included, install it using `uv add fastapi[standard]`.
* **`pydantic`**: For data validation, parsing, and settings management, ensuring data integrity.
* **`pydantic-settings`**: Manage configs and settings
* **`sqlmodel`**: A powerful SQL toolkit and Object Relational Mapper (ORM) for robust database interactions.
* **`rich`**: For generating beautiful and informative terminal output, including syntax highlighting, tables, and progress bars.
* **`typer`**: For building intuitive and powerful command-line interfaces (CLIs) with minimal code, built on top of `Click`. 
* **`pydantic-ai`**: Specifically for structured output from AI models, facilitating reliable parsing of generative AI responses.
* **`fastmcp`**: For building and running MCPs (Multi-Cloud Platforms) with ease.
* **`pyyaml`**: For parsing and generating YAML files, ensuring data integrity.

## Development

* **`ruff`**: For code quality and style checking, ensuring consistent code quality.
* **`mypy`**: For static type checking, catching type-related errors before runtime.
* **`bandit`**: For security testing, identifying potential vulnerabilities in code.
* **`mkdocs`**: For documentation, ensuring clear and up-to-date documentation.

## Testing

* **`pytest`**: For writing and running tests, ensuring code reliability.
* **`pytest-asyncio`**: For testing asynchronous code.
* **`pytest-mock`**: For mocking dependencies in tests.
* **`pytest-cov`**: For coverage reporting.
