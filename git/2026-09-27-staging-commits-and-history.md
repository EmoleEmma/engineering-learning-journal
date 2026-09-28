# Staging, Commits & History

**Date:** September 27, 2026

## What I Learned

Today I learned how Git uses the staging area and commits to record changes and maintain the history of a project.

I learned about:

- The staging area
- Staging changes with `git add`
- Creating commits
- Writing meaningful commit messages
- Viewing commit history
- `git status`
- `git diff`
- `git log`
- `git show`
- Understanding commits as points in project history

## What I Practiced

I modified files in a Git repository and used `git diff` to inspect my changes before staging them.

I then staged specific files, created commits, and used Git history commands to inspect the changes that had been recorded.

I also practiced writing commit messages that describe the purpose of each change.

## What I Understand

I now understand that Git separates the process of making changes from recording those changes in a commit.

The basic workflow is:

**Modify → Review → Stage → Commit → History**

I also understand that the staging area allows me to choose which changes should be included in a commit instead of automatically committing every change in the working directory.

## What I Still Find Difficult

I need more practice with:

- Creating focused commits
- Understanding when to stage individual files versus multiple files
- Reading detailed Git history
- Understanding how commits are connected
- Choosing clear and meaningful commit messages

## Practical Exercise

I created and modified files in a Git practice repository, reviewed the changes, staged them, created commits, and inspected the resulting history.

I also practiced using:

```bash
git status
git diff
git add
git commit
git log
git show
```

## View Exercise

[View Exercise](../small-projects/git/03-staging-commits-and-history/)

## Next Step

Next I will study Git branches, including creating branches, switching between branches, making changes independently, and merging branches.