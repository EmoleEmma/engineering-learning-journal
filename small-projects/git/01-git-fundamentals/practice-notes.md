# Git Fundamentals — Practice Notes

## Practice Session

**Date:** September 20, 2026

## Objective

Understand how Git tracks changes inside a repository.

## Commands Used

```bash
git init
git status
git add .
git diff
```

## Experiment

I created a simple practice repository and added several files.

I then modified one of the files and used `git status` and `git diff` to observe the changes.

## Observations

### Before Staging

The modified file appeared as a change in the working directory.

### After Staging

The file moved into the staging area.

This helped me understand that staging is a separate step before creating a commit.

## What I Learned

The basic Git workflow is:

**Modify → Stage → Commit**

Git allows me to inspect changes before committing them.

## Problem Encountered

I initially confused the working directory with the staging area.

## How I Solved It

I used `git status` and `git diff` repeatedly to observe the state of the repository after each command.

## Result

I can now identify whether a change is:

- Untracked
- Modified
- Staged
- Committed