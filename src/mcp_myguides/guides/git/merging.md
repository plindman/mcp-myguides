## Merging Tips

* Prefer small, focused branches to avoid conflicts.
* Resolve merge conflicts locally when they occur:

  ```

### Rebasing for a Clean History (Single Developer)

For a single developer, `git rebase` can be a powerful tool to maintain a clean, linear project history. Instead of merging, which creates a merge commit, rebasing moves your branch to the tip of another branch, effectively rewriting history. This can make your commit history much easier to read and understand.

**Benefits for a Solo Developer:**

*   **Clean, Linear History:** Avoids "merge commits" that can clutter the history.
*   **Easier Debugging:** A linear history makes tools like `git bisect` more effective.
*   **Simplified Reverts:** Reverting changes is often simpler with a linear history.

**When to Rebase:**

*   **Before merging your feature branch into `main`:** Rebase your feature branch onto the latest `main` to ensure your changes are applied on top of the most recent code.
*   **To squash commits:** Combine multiple small, incremental commits into a single, more meaningful commit.

**Basic Rebasing Workflow:**

```bash
# 1. Ensure you are on your feature branch
git checkout feat/my-feature

# 2. Fetch the latest changes from main
git fetch origin main

# 3. Rebase your feature branch onto main
git rebase main

# If conflicts occur, resolve them:
# git status
# git add <conflicted_file>
# git rebase --continue

# 4. Once rebase is complete, you can fast-forward merge into main
git checkout main
git merge feat/my-feature
```

**Important:** Never rebase commits that have already been pushed to a shared remote repository, as this can cause issues for collaborators. For a single developer, this means being careful if you've pushed your feature branch and then decide to rebase it. If you must rebase a pushed branch, you'll need to force push (`git push --force-with-lease`), but be aware of the implications.
