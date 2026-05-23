# Git Commands Reference - Practical Guide

## 1. INITIAL SETUP

### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list
```

### Initialize a Repository
```bash
git init
git clone <repository-url>
```

---

## 2. CHECKING STATUS & HISTORY

### Status
```bash
git status
git status -s
```

### View Commit History
```bash
git log
git log --oneline
git log --oneline -5
git log --graph --oneline --all
git log --author="AyanWarame"
git show <commit-hash>
```

### Compare Changes
```bash
git diff
git diff --staged
git diff <branch1> <branch2>
git diff HEAD~1
```

---

## 3. STAGING & COMMITTING

### Stage Files
```bash
git add calc.py
git add .
git add *.py
git add -A
```

### Unstage Files
```bash
git restore --staged calc.py
git reset HEAD calc.py
```

### Commit
```bash
git commit -m "Add multiply function"
git commit -am "Update calculator"
git commit --amend
git commit --amend --no-edit
```

### Discard Changes
```bash
git restore calc.py
git checkout -- calc.py
git clean -fd
```

---

## 4. BRANCHING

### List Branches
```bash
git branch
git branch -a
git branch -v
```

### Create Branch
```bash
git branch feature/multiply
git checkout -b feature/multiply
git switch -c feature/multiply
```

### Switch Branch
```bash
git checkout main
git checkout feature/multiply
git switch main
git switch feature/multiply
```

### Delete Branch
```bash
git branch -d feature/multiply
git branch -D feature/multiply
git push origin --delete feature/multiply
```

### Rename Branch
```bash
git branch -m old-name new-name
git branch -m feature/multiply feature/multiplication
```

---

## 5. MERGING

### Merge Branch
```bash
git checkout main
git merge feature/multiply
```

### Merge Abort
```bash
git merge --abort
```

### View Merge Base
```bash
git merge-base main feature/multiply
```

---

## 6. REBASING

### Rebase Branch
```bash
git checkout feature/divide
git rebase main
git rebase main feature/divide
```

### Interactive Rebase
```bash
git rebase -i HEAD~3
git rebase -i main
```

### Rebase Abort
```bash
git rebase --abort
```

### Rebase Continue
```bash
git rebase --continue
```

---

## 7. STASHING

### Stash Changes
```bash
git stash
git stash save "Work in progress on multiply"
```

### List Stashes
```bash
git stash list
```

### Apply Stash
```bash
git stash apply
git stash apply stash@{0}
git stash pop
```

### Delete Stash
```bash
git stash drop
git stash drop stash@{0}
git stash clear
```

---

## 8. REMOTE OPERATIONS

### View Remote
```bash
git remote
git remote -v
git remote show origin
```

### Add Remote
```bash
git remote add origin <repository-url>
```

### Change Remote
```bash
git remote set-url origin <new-url>
git remote remove origin
```

### Fetch
```bash
git fetch
git fetch origin
git fetch --all
```

### Pull
```bash
git pull
git pull origin main
git pull --rebase
```

### Push
```bash
git push
git push origin main
git push origin feature/multiply
git push -u origin feature/multiply
git push origin --delete feature/multiply
```

---

## 9. TAGGING

### Create Tag
```bash
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
```

### List Tags
```bash
git tag
git tag -l "v1*"
```

### View Tag
```bash
git show v1.0.0
```

### Delete Tag
```bash
git tag -d v1.0.0
git push origin --delete v1.0.0
```

### Push Tags
```bash
git push origin v1.0.0
git push origin --tags
```

---

## 10. UNDO & RESET

### Soft Reset (keep changes staged)
```bash
git reset --soft HEAD~1
```

### Mixed Reset (unstage changes)
```bash
git reset --mixed HEAD~1
git reset HEAD~1
```

### Hard Reset (discard all changes)
```bash
git reset --hard HEAD~1
git reset --hard origin/main
```

### Revert (create new commit undoing changes)
```bash
git revert <commit-hash>
git revert HEAD
```

---

## 11. SEARCHING & FINDING

### Search Commit Messages
```bash
git log --grep="multiply"
git log --grep="function"
```

### Search Code
```bash
git log -p -S "multiply"
git log -p --all -S "def multiply"
```

### Find Commit
```bash
git log --oneline | grep "Add"
git log --reverse --oneline -5
```

### Blame
```bash
git blame calc.py
git blame -L 5,10 calc.py
```

---

## 12. ADVANCED OPERATIONS

### Cherry Pick
```bash
git cherry-pick <commit-hash>
git cherry-pick feature/multiply
```

### Squash Commits
```bash
git rebase -i HEAD~3
# Mark commit as 'squash' or 's'
```

### Create Patch
```bash
git diff > changes.patch
git apply changes.patch
```

### Bisect (Find problematic commit)
```bash
git bisect start
git bisect bad
git bisect good <commit-hash>
git bisect reset
```

### Reflog (Recover lost commits)
```bash
git reflog
git checkout <lost-commit-hash>
```

---

## 13. PRACTICAL WORKFLOW EXAMPLES

### Feature Branch Workflow
```bash
# Create feature branch
git checkout -b feature/multiply

# Make changes
# ... edit calc.py, add multiply function ...

# Stage and commit
git add calc.py
git commit -m "Add multiply function"

# Switch to main
git checkout main

# Merge feature
git merge feature/multiply

# Delete feature branch
git branch -d feature/multiply

# Push to remote
git push origin main
```

### Pull Request Workflow
```bash
# Create branch
git checkout -b feature/divide

# Make changes and commit
git add calc.py
git commit -m "Add divide function"

# Push to remote
git push -u origin feature/divide

# Create PR on GitHub/GitLab (via web UI)

# After approval, merge and delete
git checkout main
git pull origin main
git merge feature/divide
git push origin main
git branch -d feature/divide
```

### Handling Merge Conflicts
```bash
# During merge conflict
git merge feature/multiply
# CONFLICT occurs

# Check conflicted files
git status

# View conflicts
cat calc.py

# Edit calc.py to resolve conflicts

# Stage resolved file
git add calc.py

# Complete merge
git commit -m "Resolve merge conflict"
```

### Undo Last Commit (not pushed)
```bash
git reset --soft HEAD~1
# Changes are now staged, can edit and recommit
git add .
git commit -m "Fixed commit message"
```

### Undo Last Pushed Commit
```bash
git revert HEAD
# Creates new commit that undoes changes
git push origin main
```

### Sync Fork with Main Repository
```bash
git remote add upstream <original-repo-url>
git fetch upstream
git checkout main
git rebase upstream/main
git push origin main
```

---

## 14. USEFUL SHORTCUTS & ALIASES

### Create Aliases
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.log1 "log --oneline -5"
git config --global alias.unstage "restore --staged"
git config --global alias.undo "reset --soft HEAD~1"
```

### Use Aliases
```bash
git st
git co main
git br
git ci -m "message"
```

---

## 15. QUICK REFERENCE CHEAT SHEET

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

---

## Tips
- Always `git pull` before starting new work
- Use descriptive commit messages
- Commit frequently with logical groupings
- Use branches for new features
- Review changes before committing: `git diff`
- Don't force push unless necessary: `git push --force-with-lease`
