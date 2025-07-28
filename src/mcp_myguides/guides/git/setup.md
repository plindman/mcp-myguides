# Repo setup

## Switch github account if needed

```bash

# Make sure the right user is active
git-set-active-user [username]

# Get the user name of the active account
git-get-active-user

# Used Github CLi commands
gh auth status
gh auth switch
```

## Git config

```bash
git-set-repo-user $(git-get-active-user)
```

## 