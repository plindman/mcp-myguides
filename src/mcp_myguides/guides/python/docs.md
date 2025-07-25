## 7. Documentation

* **User Documentation:** Any changes to user-facing functionality should be reflected in the `docs/` directory and in the project README.md.
* **Internal Documentation:** Maintain clear internal documentation for complex logic, architecture decisions, and design patterns.
* **API Documentation:** Use tools like Swagger or OpenAPI to document your API endpoints.

mkdocs is used for documentation. Install it using:
```bash
uv add --dev mkdocs
```

To build the docs, run:
```bash
uv run mkdocs build
```
