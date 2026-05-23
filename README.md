# Calculator - Git Learning Project

A simple calculator script designed for practicing Git operations and workflows.

## Features

- **add(a, b)** - Adds two numbers
- **subtract(a, b)** - Subtracts two numbers

## Getting Started

Run the calculator:
```bash
python calc.py
```

## Git Learning Exercises

Here are some exercises to practice Git operations:

### 1. Create a Multiplication Branch
```bash
git checkout -b feature/multiply
# Add a multiply() function to calc.py
git add calc.py
git commit -m "Add multiply function"
git checkout main
git merge feature/multiply
```

### 2. Create a Division Branch
```bash
git checkout -b feature/divide
# Add a divide() function to calc.py
git add calc.py
git commit -m "Add divide function"
```

### 3. Practice Rebasing
```bash
# While on feature/divide branch
git rebase main
```

### 4. Create Multiple Commits
```bash
git checkout -b feature/square
# Commit 1: Add square() function
# Commit 2: Update main() to use square()
git log --oneline
```

### 5. Stashing Changes
```bash
# Make changes to calc.py
git stash
# Make other changes on another branch
git stash pop
```

## Perfect for Practicing

- Branching (`git checkout -b`)
- Merging (`git merge`)
- Rebasing (`git rebase`)
- Committing (`git add`, `git commit`)
- Branch switching (`git checkout`)
- Viewing history (`git log`)
- And more!
