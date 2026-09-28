# Repositories & Working with Git — Practice Notes

## Objective

Understand the difference between creating a repository and cloning an existing repository.

## Experiment 1 — `git init`

I created a project directory and initialized Git inside it.

```bash
git init
```

Git created the repository metadata required to track the project.

## Experiment 2 — `git clone`

I cloned an existing GitHub repository.

```bash
git clone <repository-url>
```

This created a local copy of the remote repository.

## Comparison

### `git init`

Used when I already have a project locally and want to begin tracking it with Git.

### `git clone`

Used when a repository already exists and I want a local copy of it.

## What I Learned

The important difference is where the repository starts.

**`git init` → Local project → Git repository**

**`git clone` → Existing repository → Local copy**

## Questions I Still Have

- How does Git store commits internally?
- How are local and remote branches connected?
- What exactly happens during `git fetch`?

These will be explored in later topics.