# Git Development Guidelines Overview

This section provides a comprehensive overview of the Git development guidelines, designed to ensure consistency, quality, and efficiency across our projects. These guidelines cover various aspects of the development lifecycle, from setting up your repository to deploying and maintaining your applications.

## Core Git Rules

*   Always ensure that `.gitignore` is up-to-date and includes all essential exclusions. Be especially careful with secrets.
*   Never commit directly to `main`.
*   Always create a **separate branch** for each feature or fix.
*   Once your work is complete and tested, **merge it into `main` locally**.
*   After merging, run your tests to verify nothing is broken. Optionally run the app manually if needed.
*   Keep commit messages clear and focused.

## Key Areas Covered:

*   **.gitignore:** Learn how to manage the `.gitignore` file to keep the repository clean.
    *   Tags: `git`, `git/gitignore`
*   **Workflow:** Learn about our standards for branching, merging, and our simple Git workflow.
    *   Tags: `git`, `git/workflow`
*   **Commit Messages:** Understand how to effectively write clear and structured commit messages.
    *   Tags: `git`, `git/commit-messages`
*   **Merging:** Discover the recommended practices for merging branches and resolving conflicts.
    *   Tags: `git`, `git/merging`
*   **Troubleshooting:** Find solutions to common Git issues and how to recover from mistakes.
    *   Tags: `git`, `git/troubleshooting`

By following these guidelines, we aim to foster a collaborative and productive development environment, leading to high-quality and maintainable applications.
