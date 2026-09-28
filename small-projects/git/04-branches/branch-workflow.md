# Branch Workflow

## Objective

Practice a simple feature-branch workflow.

## Starting Point

The project begins on:

```text
main
```

## Step 1 — Create Feature Branch

```bash
git switch -c feature/add-documentation
```

The project is now being developed on:

```text
feature/add-documentation
```

## Step 2 — Make Changes

I made the required documentation changes.

## Step 3 — Review Changes

```bash
git status
git diff
```

## Step 4 — Commit

```bash
git add .
git commit -m "docs: add project documentation"
```

## Step 5 — Return to Main

```bash
git switch main
```

## Step 6 — Merge

```bash
git merge feature/add-documentation
```

## Step 7 — Delete the Feature Branch

```bash
git branch -d feature/add-documentation
```

## Final Workflow

```text
main
 │
 ├── feature/add-documentation
 │        │
 │        ├── Make changes
 │        ├── Review
 │        └── Commit
 │
 └── Merge back into main
```

## What I Learned

A branch allows work to be isolated from the main branch.

The branch can be reviewed and tested before its changes are merged into `main`.

## Real-World Connection

This workflow is similar to how feature work can be developed separately before being integrated into the main codebase.

## Result

I successfully practiced:

- Creating a branch
- Switching branches
- Making changes
- Committing changes
- Returning to `main`
- Merging a branch
- Deleting the completed branch