### ✅ Merging Tips

* Prefer small, focused branches to avoid conflicts.
* Resolve merge conflicts locally when they occur:

  ```bash
  git status          # See which files are conflicted
  
  # Use git diff or less to inspect conflicts. 
  # Conflicted files contain <<<<<<< HEAD markers to search for.
  # Edit the files to fix the conflict

  git add .
  git commit          # Finalize the merge
  ```
