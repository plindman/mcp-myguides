# End-to-End Testing with Playwright

Playwright is primarily used for testing web applications. It is an open-source automation library developed by Microsoft for testing web applications. It enables reliable end-to-end testing across modern browsers with a single API. 
The Python version supports Chromium, Firefox, and WebKit, making it a robust alternative to Selenium or other legacy tools.

**Best Practices**

* **Use Fixtures:** Utilize pytest fixtures to manage setup and teardown processes for your tests.
* **Organize Tests:** Structure your tests to mirror user workflows, making them more readable and maintainable.
* **Handle Asynchronous Operations:** Playwright automatically waits for elements to be ready before interacting with them, reducing the need for manual waits.
* **Parallel Execution:** Leverage Playwright's ability to run tests in parallel to speed up your test suite.
* **Continuous Integration:** Integrate your E2E tests into your CI/CD pipeline to catch issues early in the development process.

For more detailed guidance on using Playwright with Python, refer to the official documentation: [Playwright for Python](https://playwright.dev/python/).

**Install Playwright and its CLI:**

   ```bash
   uv add --dev pytest-playwright
   uv run playwright install # Installs browser binaries
   ```

**Running Tests**

Execute your tests using the following command:

```bash
# This command runs all tests located in the `tests/e2e` directory.
uv run pytest tests/e2e
```