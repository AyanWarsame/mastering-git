# Git Commands Reference - Comprehensive Practical Guide

## ── SETUP ──

### Configure Git
```bash
# Set your name globally
git config --global user.name "Your Name"

# Set your email globally
git config --global user.email "you@email.com"

# Set VS Code as default editor
git config --global core.editor "code --wait"

# Set VS Code as merge tool
git config --global merge.tool vscode

# Default pull to rebase (recommended)
git config --global pull.rebase true

# Show all config settings
git config --list
```

### Useful Aliases
```bash
# Quick status
git config --global alias.st status

# Quick checkout
git config --global alias.co checkout

# Quick branch listing
git config --global alias.br branch

# Quick commit
git config --global alias.ci commit

# Pretty log with graph
git config --global alias.lg "log --oneline --graph --decorate"
```

---

## ── INIT & CLONE ──

### Initialize Repository
```bash
# Initialise a new repo in current directory
git init

# Initialise a new repo in a new folder
git init my-project

# Clone a remote repo
git clone https://github.com/user/repo.git

# Clone into a specific folder
git clone https://github.com/user/repo.git my-folder

# Shallow clone (latest snapshot only)
git clone --depth 1 https://github.com/user/repo.git

# Clone and checkout a specific branch
git clone --branch develop https://github.com/user/repo.git
```

---

## ── STAGE & COMMIT ──

### Check Status
```bash
# Show working tree status (detailed)
git status

# Show status in short format
git status -s
```

### Stage Files
```bash
# Stage all changes in current directory
git add .

# Stage a specific file
git add calc.py

# Stage changes interactively (hunk by hunk)
git add -p

# Stage all changes everywhere (-A = all)
git add -A
```

### Commit
```bash
# Commit with a message
git commit -m "feat: add login endpoint"

# Edit the last commit message
git commit --amend -m "corrected message"

# Add staged changes to last commit, keep message
git commit --amend --no-edit

# Create a fixup commit for the previous commit
git commit --fixup HEAD~1
```

### Unstage & Discard
```bash
# Unstage a specific file (keep changes)
git reset HEAD src/app.js

# Discard changes in working tree for a file
git checkout -- src/app.js

# Restore file to last commit state (modern syntax)
git restore src/app.js

# Unstage a file (modern syntax)
git restore --staged src/app.js

# Delete all untracked files and directories
git clean -fd
```

### View Changes
```bash
# Show unstaged changes
git diff

# Show staged changes (about to be committed)
git diff --staged

# Show changes between last two commits
git diff HEAD~1 HEAD

# Compare two branches
git diff main..develop
```

---

## ── BRANCHES ──

### List Branches
```bash
# List local branches
git branch

# List all branches (local + remote)
git branch -a

# List remote branches only
git branch -r

# List branches with details
git branch -v
```

### Create & Switch
```bash
# Create a new branch (stay on current)
git branch feature/login

# Create and switch to a new branch
git checkout -b feature/login

# Create and switch (modern syntax)
git switch -c feature/login

# Switch to an existing branch
git checkout develop

# Switch branch (modern syntax)
git switch develop

# Track a remote branch locally
git checkout -b feature/login origin/feature/login
```

### Rename & Delete
```bash
# Rename a branch
git branch -m old-name new-name

# Delete a merged branch (safe)
git branch -d feature/login

# Force delete a branch (even if unmerged)
git branch -D feature/login

# Delete a remote branch
git push origin --delete feature/login
```

---

## ── REMOTE ──

### View Remote
```bash
# List remote connections
git remote

# List remote connections with URLs
git remote -v

# Show detailed info about a remote
git remote show origin
```

### Manage Remote
```bash
# Add a remote named origin
git remote add origin https://github.com/user/repo.git

# Rename a remote
git remote rename origin upstream

# Remove a remote
git remote remove origin

# Change remote URL
git remote set-url origin https://github.com/user/repo.git
```

### Fetch, Pull & Push
```bash
# Download all remote changes (don't merge)
git fetch origin

# Fetch from all remotes
git fetch --all

# Fetch + merge remote branch into current
git pull origin develop

# Fetch + rebase (cleaner history)
git pull --rebase origin develop

# Push a branch to remote
git push origin feature/login

# Push and set upstream tracking
git push -u origin feature/login

# Safe force push (won't overwrite others' work)
git push --force-with-lease origin feature/login

# Push commits + all tags
git push origin main --tags

# Push multiple branches + tags
git push origin main develop --tags
```

---

## ── MERGE & REBASE ──

### Merge
```bash
# Merge branch into current (fast-forward if possible)
git merge feature/login

# Merge and always create a merge commit
git merge --no-ff feature/login

# Squash all commits into one before merging
git merge --squash feature/login

# Abort an in-progress merge
git merge --abort
```

### Rebase
```bash
# Rebase current branch onto develop
git rebase develop

# Rebase onto the remote develop
git rebase origin/develop

# Interactive rebase: edit last 3 commits
git rebase -i HEAD~3

# Rebase + auto-apply fixup! commits
git rebase -i --autosquash origin/develop

# Continue after resolving a conflict
git rebase --continue

# Abort an in-progress rebase
git rebase --abort

# Skip the current conflicting commit and continue
git rebase --skip
```

### Cherry Pick
```bash
# Apply a specific commit to current branch
git cherry-pick a1b2c3d

# Apply a range of commits
git cherry-pick a1b2c3d..e4f5g6h
```

---

## ── LOG & HISTORY ──

### View History
```bash
# Full commit history
git log

# Compact one-line log
git log --oneline

# Visual branch graph (all branches)
git log --oneline --graph --decorate --all

# Last 10 commits
git log -10 --oneline

# Show details of a specific commit
git show a1b2c3d

# Show a file as it was at a specific commit
git show a1b2c3d:src/app.js
```

### Search History
```bash
# Commits by a specific author
git log --author="Alice"

# Commits from the last 2 weeks
git log --since="2 weeks ago"

# Search commits by message keyword
git log --grep="fix:"

# Commits that touched a specific file
git log src/app.js

# Commits + diffs for a specific file
git log -p src/app.js

# Show who changed each line of a file
git blame src/app.js

# Commit count per author (sorted)
git shortlog -sn
```

---

## ── UNDO & RESET ──

### Revert
```bash
# Create a new commit that undoes a commit (safe for shared branches)
git revert a1b2c3d

# Revert a merge commit (m 1 = keep the first parent)
git revert -m 1 HEAD
```

### Reset
```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset --mixed HEAD~1

# Undo last commit and DISCARD all changes
git reset --hard HEAD~1

# Reset to remote state
git reset --hard origin/main

# Go back to state before last merge/rebase
git reset --hard ORIG_HEAD
```

### Recover Lost Work
```bash
# Show full history including resets (your safety net)
git reflog

# Show reflog for all branches
git reflog show --all

# Restore a file from a specific commit
git checkout a1b2c3d -- src/app.js

# Create a branch from a reflog entry
git checkout -b recovery a1b2c3d
```

---

## ── STASH ──

### Save Work Temporarily
```bash
# Stash all uncommitted changes
git stash

# Stash with a description
git stash push -m "WIP: login form"

# Stash a specific file
git stash push src/app.js -m "partial api work"
```

### Manage Stashes
```bash
# List all stashes
git stash list

# Show diff of latest stash
git stash show -p

# Apply latest stash and remove it from stash list
git stash pop

# Apply a specific stash (keep it in list)
git stash apply stash@{2}

# Delete a specific stash
git stash drop stash@{0}

# Delete ALL stashes
git stash clear

# Create a branch from a stash
git stash branch feature/login
```

---

## ── TAGS ──

### Create Tags
```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag (recommended)
git tag -a v1.0.0 -m "Release 1.0.0"

# Tag a specific past commit
git tag -a v1.0.1 a1b2c3d -m "Hotfix"
```

### Manage Tags
```bash
# List all tags
git tag

# Filter tags by pattern
git tag -l "v1*"

# Show tag details
git show v1.0.0

# Show the most recent tag reachable from current commit
git describe --tags

# Delete a local tag
git tag -d v1.0.0

# Delete a remote tag
git push origin --delete v1.0.0

# Checkout code at a specific tag (detached HEAD)
git checkout v1.0.0
```

### Push Tags
```bash
# Push a single tag to remote
git push origin v1.0.0

# Push ALL tags to remote
git push origin --tags
```

---

## ── GITFLOW ──

### Gitflow Workflow
```bash
# Initialise GitFlow with default settings
git flow init -d

# Start a feature branch off develop
git flow feature start my-feature

# Merge feature into develop, delete branch
git flow feature finish my-feature

# Push feature branch to remote
git flow feature publish my-feature

# Pull a remote feature branch
git flow feature pull origin my-feature

# Cut a release branch off develop
git flow release start 1.0.0

# Merge release into main + develop, tag it
git flow release finish 1.0.0

# Start a hotfix branch off main
git flow hotfix start fix-login

# Merge hotfix into main + develop, tag it
git flow hotfix finish fix-login

# List all feature branches
git flow feature list

# List all release branches
git flow release list
```

---

## ── CONFLICTS ──

### Handle Merge Conflicts
```bash
# See which files have conflicts
git status

# Show only conflicted files
git diff --diff-filter=U

# List all unresolved files (names only)
git diff --name-only --diff-filter=U

# Open the configured visual merge tool
git mergetool

# Mark a conflict as resolved
git add src/app.js

# Keep YOUR version of a conflicted file
git checkout --ours src/app.js

# Keep THEIR version of a conflicted file
git checkout --theirs src/app.js

# Show commits that caused the conflict
git log --merge --oneline

# Abort merge and return to pre-merge state
git merge --abort

# Abort rebase and return to pre-rebase state
git rebase --abort
```

---

## ── INSPECT & SEARCH ──

### Search & Inspect
```bash
# Search for a string in tracked files
git grep "TODO" src/

# Search with line numbers
git grep -n "function addTask"

# Find commits that added/removed a string (pickaxe)
git log -S "addTask" --oneline

# List all tracked files
git ls-files

# List all untracked files
git ls-files --others --exclude-standard

# Show repo size and object count
git count-objects -vH
```

### Binary Search for Bugs
```bash
# Start binary search to find a bug
git bisect start

# Mark current commit as bad (has the bug)
git bisect bad

# Mark a known good commit
git bisect good v0.9.0

# End bisect session and return to HEAD
git bisect reset
```

---

## ── ADVANCED ──

### Worktrees & Submodules
```bash
# Check out a second branch without losing current work
git worktree add ../hotfix main

# List all worktrees
git worktree list

# Add a submodule
git submodule add https://github.com/user/lib.git libs/lib

# Clone and initialise all submodules
git submodule update --init --recursive
```

### Patches & Bundling
```bash
# Create a diff patch file
git diff > patch.diff

# Apply a diff patch file
git apply patch.diff

# Export last 3 commits as patch files
git format-patch HEAD~3

# Email patches to maintainers (mailing list workflow)
git send-email *.patch

# Bundle entire repo into one file (for offline transfer)
git bundle create repo.bundle --all
```

### Maintenance & Verification
```bash
# Run garbage collection to optimise the repo
git gc --aggressive

# Verify integrity of the object database
git fsck

# Attach a note to a commit
git notes add -m "reviewed by Alice" a1b2c3d

# Export repo as a zip (no .git folder)
git archive --format=zip HEAD > release.zip
```

---

## ── GITHUB CLI ──

### Authenticate & Create
```bash
# Authenticate with GitHub
gh auth login

# Create a new GitHub repo
gh repo create my-app --public

# Clone a GitHub repo
gh repo clone user/repo
```

### Pull Requests
```bash
# Create a new pull request
gh pr create --base develop --title "feat: login"

# List open pull requests
gh pr list

# View PR details
gh pr view 42

# Check out a PR locally for testing
gh pr checkout 42

# Approve a PR
gh pr review 42 --approve

# Request changes on a PR
gh pr review 42 --request-changes -b "Needs tests"

# Merge and delete a PR's branch
gh pr merge 42 --squash --delete-branch
```

### Issues & Releases
```bash
# Create a GitHub issue
gh issue create --title "Bug: null user" --body "Steps to reproduce..."

# List issues by label
gh issue list --label "bug"

# Create a GitHub release
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"
```

### Workflows
```bash
# Manually trigger a GitHub Actions workflow
gh workflow run deploy.yml

# List recent workflow runs
gh run list
```

---

## ── QUICK REFERENCE CHEAT SHEET ──

| Command | Description |
|---------|-------------|
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit changes |
| `git push` | Push to remote |
| `git pull` | Pull from remote |
| `git checkout -b feature` | Create & switch branch |
| `git merge feature` | Merge branch |
| `git log --oneline` | View compact history |
| `git diff` | Show unstaged changes |
| `git reset --hard HEAD~1` | Undo last commit |
| `git stash` | Save work temporarily |
| `git rebase main` | Rebase onto main |
| `git tag v1.0.0` | Create a tag |
| `git remote -v` | List remotes |
| `git reflog` | Show complete history |

---

## Tips
- Always `git pull` before starting new work
- Use descriptive commit messages (feat:, fix:, docs:, etc.)
- Commit frequently with logical groupings
- Use branches for new features (feature/name)
- Review changes before committing: `git diff`
- Don't force push unless necessary: `git push --force-with-lease`
- Pull with rebase for cleaner history: `git pull --rebase`
