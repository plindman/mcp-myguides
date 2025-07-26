# Git Workflow

We use a simple Git workflow focused on **local branches and direct merges into `main`**.

## ✅ Typical Git Workflow

```bash
# 1. Update main
git checkout main
git pull

# 2. Create a new branch for your work
git checkout -b feat/my-feature

# 3. Do your work and commit as needed
git add .
git commit -m "feat: add user login flow"

# 4. Merge your changes back to main
git checkout main
git diff feat/my-feature
git merge feat/my-feature

# 5. Delete your branch (optional)
git branch -d feat/my-feature
```