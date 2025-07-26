## Git Troubleshooting

This section provides solutions to common Git issues you might encounter.

### 1. Undoing the Last Commit

If you need to undo the very last commit, but keep the changes in your working directory:

```bash
git reset HEAD~1
```

If you want to undo the last commit and discard the changes:

```bash
git reset --hard HEAD~1
```

### 2. Reverting a Specific Commit

To undo a commit that happened earlier in history (not necessarily the last one), you can use `git revert`. This creates a *new* commit that undoes the changes of the specified commit, preserving the history.

```bash
git revert <commit-hash>
```

### 3. Fixing a Detached HEAD

A detached HEAD state occurs when you check out a specific commit rather than a branch. To get back to a branch:

```bash
# Option 1: Create a new branch from the detached HEAD
git checkout -b <new-branch-name>

# Option 2: Move to an existing branch (discarding detached HEAD changes)
git checkout <existing-branch-name>
```

### 4. Amending the Last Commit

If you forgot to add a file or made a typo in your last commit message, you can amend it:

```bash
git add <forgotten-file>
git commit --amend
```

This will open your editor to modify the commit message. If you only want to change the message:

```bash
git commit --amend -m "New commit message"
```

### 5. Removing a File from Git History (Caution!)

If you accidentally committed a sensitive file (e.g., a password file) and need to remove it from the entire history, use `git filter-branch` or `BFG Repo-Cleaner`. **Use with extreme caution**, as this rewrites history and can cause issues for collaborators.

```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <path-to-your-file>" \
  --prune-empty --tag-name-filter cat -- --all
```

For more robust removal, consider `BFG Repo-Cleaner` (search online for its usage).

### 6. Stashing Changes

If you need to switch branches but have uncommitted changes you want to save for later, use `git stash`:

```bash
git stash save "Work in progress on feature X"
# ... switch branches, do other work ...
git stash pop
```

To see your stashes:

```bash
git stash list
```

To apply a specific stash without removing it from the stash list:

```bash
git stash apply stash@{1}
```