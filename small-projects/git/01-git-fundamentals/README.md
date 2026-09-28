# Git Fundamentals

## Objective

Practice the basic Git workflow and understand how Git tracks changes in a project.

## Concepts Practiced

- Git repositories
- Working directory
- Staging area
- Git status
- Git diff
- Tracking files
- Staging files
- Basic Git configuration

## Tasks

### 1. Create a Repository

Initialize a new Git repository.

```bash
git init
```

### 2. Create Files

Create a few practice files and check the repository status.

```bash
git status
```

### 3. Track Changes

Stage the files.

```bash
git add .
```

Check the status again.

```bash
git status
```

### 4. Inspect Changes

Modify one of the files and inspect the changes.

```bash
git diff
```

### 5. Stage the Changes

Stage the modified file.

```bash
git add <filename>
```

## What I Observed

I observed how Git moves files through different states:

**Untracked → Staged → Committed**

I also observed the difference between changes in the working directory and changes that have been staged.

## Commands Practiced

```bash
git init
git status
git add
git diff
```

## What I Learned

Git does not automatically commit every change I make.

Changes must be intentionally staged and committed.

Understanding the working directory and staging area makes the basic Git workflow much easier to understand.

## Evidence

- Repository created
- Files tracked
- Changes staged
- `git status` used
- `git diff` used
- Git history created

## Next

Next I will practice repositories and working with Git.