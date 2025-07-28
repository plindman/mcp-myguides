# Polyglot Monorepo Setup Guide

- **Unified Development**: Single command to run both frontend and backend
- **Fast Tooling**: Bun and uv provide incredibly fast package management and builds
- **Code Quality**: Automated linting and formatting across both languages
- **Containerized**: Consistent development environment with Docker
- **Modern Stack**: Latest tools optimized for developer experience

## Tools Overview

### Monorepo
- **Bun** - JavaScript runtime, package manager, task runner for TypeScript frontend
- **pre-commit** - Git hooks for automated code quality checks
- **Docker** - Containerization platform for consistent development environments
- **Docker Compose** - Multi-container orchestration for running both services together

### Frontend/Typescript
- **Bun** - JavaScript runtime, package manager, task runner for TypeScript frontend
- **Biome** - TypeScript/JavaScript linter and formatter for frontend

### Backend/Python
- **uv** - Python package manager and virtual environment manager for Python backend
- **Ruff** - Python linter and formatter for backend
- **mypy** - Python static type checker


## Project Structure

### Critical Rule: Use Project Root Directory

**⚠️ NEVER create an additional monorepo folder within the project root.** The project root directory IS the monorepo. All packages, apps, and configuration should be organized directly under the root.

```
my-monorepo-project/
├── apps/
│   ├── frontend/
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/
│   └── backend/
│       ├── pyproject.toml
│       ├── uv.lock
│       └── src/
├── logs/                 # Background service logs
├── .pids/               # Process ID files for background services
├── package.json          # Root workspace config
├── docker-compose.yml    # Local development setup
├── .gitignore           # Git ignore patterns for both languages
├── .editorconfig        # Consistent code formatting
├── .pre-commit-config.yaml # Code quality hooks
├── biome.json           # Frontend linting config
└── README.md            # Project documentation
```

The root folder contains the monorepo configuration and shared tooling that coordinates both frontend and backend applications. This includes a `package.json` file with Bun workspace configuration and scripts to run tasks across both apps in parallel or sequence, a `docker-compose.yml` file for local development that orchestrates both services, shared configuration files like `.gitignore` (covering both Node.js and Python patterns), `.editorconfig` for consistent code formatting, and `.pre-commit-config.yaml` for automated code quality checks across both languages. Additional root-level files may include environment configuration (`.env` files), documentation (`README.md`), and CI/CD pipeline definitions that handle building and testing both the TypeScript frontend and Python backend from a single workflow.

# Setup

Use tag "monorepo/setup" for details about setting up the monorepo project. 

# Development

Use tag "monorepo/dev" for details about development commands. 

# Code Quality

Use tag "monorepo/quality" for details about code quality commands. 
