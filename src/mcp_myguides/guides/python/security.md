# Security

## Secrets and Configuration Management

Proper secrets and environment configuration handling is essential for security and portability. This project follows the 12-factor app principle of separating config from code using environment variables (https://12factor.net/config).

### Tools

* **[`pydantic-settings`](https://docs.pydantic.dev/latest/integrations/settings/)**: Used to define and load application settings from environment variables (and `.env` files).
* **`.env` / `.env.example`**: Local file for non-secret config and local development settings.

#### Guidelines

**✅ Define settings with `pydantic-settings`**

* Create a central settings module (e.g. `src/core/settings.py`):
* Use `settings` throughout your application to access values in a strongly-typed and validated way.

**✅ Use `.env` for local secrets**

* Never commit actual secrets to `.env`. Use it **locally only**.
* Share structure and required variables via `.env.example`.

**✅ Git Hygiene**

Ensure `.env` is present in your `.gitignore`. This prevents accidental check-in of sensitive configuration.

#### Tips

* For production, pass secrets via actual environment variables (e.g. in Docker or CI).
* Avoid placing long-lived secrets in source control or long-lived `.env` files—use secret managers for production (e.g. AWS Secrets Manager, Vault, or Doppler).

### Security Analysis

*   We use `Bandit` to identify common security vulnerabilities in our Python code.
*   Bandit Getting started here: https://bandit.readthedocs.io/en/latest/start.html

