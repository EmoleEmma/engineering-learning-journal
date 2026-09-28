# Staging, Commits & History

## Objective

Understand how changes are staged, committed, and recorded in Git history.

## Concepts Practiced

- Staging
- Commits
- Commit messages
- `git status`
- `git diff`
- `git log`
- `git show`
- Commit history

## Tasks

### 1. Make a Change

Modify a file inside the repository.

### 2. Inspect the Change

```bash
git diff
```

### 3. Stage the Change

```bash
git add <filename>
```

### 4. Create a Commit

```bash
git commit -m "docs: update practice notes"
```

### 5. Inspect History

```bash
git log
```

### 6. Inspect a Commit

```bash
git show <commit>
```

## Commit Practice

I practiced writing commit messages that describe the purpose of a change.

Examples:

```text
docs: add Git fundamentals notes
feat: add practice example
fix: correct repository instructions
```

## What I Learned

A commit represents a recorded point in the history of a repository.

The staging area allows me to choose which changes should be included in a commit.

## Git Workflow

```text
Modify
   ↓
Review
   ↓
Stage
   ↓
Commit
   ↓
History
```

## Evidence

- Created commits
- Inspected commit history
- Used `git diff`
- Used `git log`
- Used `git show`
- Practiced meaningful commit messages

## Next

Next I will practice Git branches.