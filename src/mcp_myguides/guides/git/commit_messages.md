## Commit Message Format

Use clear, structured commit messages:

* `feat:` – New feature
* `fix:` – Bug fix
* `docs:` – Documentation
* `refactor:` – Code cleanup or internal changes
* `test:` – Adding or updating tests
* `chore:` – Miscellaneous changes (e.g. config, tooling)

Example:

```
fix: handle empty user input in login
```

## Best Practices for Commit Messages

*   **Keep the subject line concise:** Aim for 50 characters or less.
*   **Use the imperative mood:** Start the subject line with an action verb (e.g., "Add feature," "Fix bug").
*   **Provide a blank line:** Separate the subject from the body with a blank line.
*   **Explain the "why":** Use the body of the commit message to explain *why* the change was made, not just *what* was changed. This is crucial for future understanding.
*   **Limit line length:** Wrap the body at around 72 characters for readability.
*   **Reference issues (optional):** If using an issue tracker, reference the issue number in the commit message (e.g., `Fix #123`).