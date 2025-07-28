# Monorepo Setup

## Initialize Root Workspace

Create a `package.json` at the root with Bun workspace configuration:
TODO: create template file

## Configure Frontend (TypeScript)

`apps/frontend/package.json`.
TODO: commands to create file

## Configure Backend (Python)

`apps/backend/pyproject.toml`:
TODO: commands to create file

## Set Up Code Quality

Create `biome.json` for frontend linting:
TODO: create template file

Configure `pyproject.toml` for backend code quality:
TODO: create template file

## Set Up Repo Git

Create `.gitignore` with :
- Bun
- Python
- Virtual environments
- Background processes (logs, .pids)
- Common IDE files (.vscode, ...)
- Common OS files (.DS_Store, ...)
- Environment variables (.env, ...)
- Build outputs (dist/, build/, ...)
TODO: create template file

Create `.pre-commit-config.yaml`:
TODO: create template file

Install pre-commit hooks `pre-commit install`

## Set Up Docker

Create `docker-compose.yml` with frontend, backend and other needed services.
TODO: template file