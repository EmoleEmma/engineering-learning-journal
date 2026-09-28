# Repositories & Working with Git

## Objective

Practice creating and working with local Git repositories and understand how Git repositories relate to project directories.

## Concepts Practiced

- Local repositories
- `git init`
- `git clone`
- Working directory
- `.git` directory
- Tracked files
- Untracked files
- Repository status

## Tasks

### 1. Initialize a Repository

Create a new project directory and initialize Git.

```bash
git init
```

### 2. Inspect the Repository

Check the repository status.

```bash
git status
```

Inspect the repository structure and identify the `.git` directory.

### 3. Track Project Files

Create files and add them to Git.

```bash
git add .
```

### 4. Clone an Existing Repository

Clone a repository from GitHub.

```bash
git clone <repository-url>
```

### 5. Compare the Two Workflows

Compare:

```bash
git init
```

with:

```bash
git clone <repository-url>
```

## What I Learned

`git init` creates a new Git repository inside an existing project.

`git clone` creates a local copy of an existing repository.

## Key Difference

| Command | Purpose |
|---|---|
| `git init` | Create a new repository |
| `git clone` | Copy an existing repository |

## What I Understand

I now understand that Git can be introduced into an existing project with `git init`, while `git clone` is normally used when starting from an existing remote repository.

## Evidence

- Created a local repository
- Cloned an existing repository
- Checked repository status
- Worked with tracked and untracked files

## Next

Next I will practice staging, commits, and Git history.