# Git Branches

## Objective

Understand how branches allow changes to be developed separately from the main branch.

## Concepts Practiced

- `main`
- Branches
- Feature branches
- Creating branches
- Switching branches
- Merging branches
- Branch naming
- Deleting branches

## Basic Workflow

```text
main
 ↓
Create feature branch
 ↓
Make changes
 ↓
Commit changes
 ↓
Merge into main
```

## Commands Practiced

### View Branches

```bash
git branch
```

### Create a Branch

```bash
git branch feature/example
```

### Switch Branches

```bash
git switch feature/example
```

### Create and Switch

```bash
git switch -c feature/example
```

### Merge a Branch

```bash
git switch main
git merge feature/example
```

### Delete a Branch

```bash
git branch -d feature/example
```

## Practical Exercise

I created a feature branch from `main`.

I made changes on the feature branch without directly changing the main branch.

I committed the changes and merged the feature branch back into `main`.

## What I Learned

Branches provide a separate line of development.

They allow developers to work on features, fixes, or experiments without immediately changing the main branch.

## What I Still Need to Practice

- Larger branch workflows
- Remote branches
- Pull requests
- Rebasing
- More complex merge conflicts

## Evidence

- Feature branch created
- Changes made on branch
- Commits created
- Branch merged into `main`

## Next

Next I will practice more advanced merging and conflict resolution.