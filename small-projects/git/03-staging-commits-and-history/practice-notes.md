# Staging, Commits & History — Practice Notes

## Objective

Practice creating commits and inspecting repository history.

## Experiment

I modified a file and inspected the change.

```bash
git diff
```

I then staged the file.

```bash
git add README.md
```

I created a commit.

```bash
git commit -m "docs: update README"
```

I inspected the history.

```bash
git log
```

## What I Observed

The commit became part of the repository history.

I could then use Git commands to inspect when the commit was created and what changes it contained.

## Commands Practiced

```bash
git status
git diff
git add
git commit
git log
git show
```

## What I Learned

The staging area gives me control over what goes into a commit.

I also learned that commit messages should explain the purpose of the change.

## Improvement

Instead of creating large commits containing unrelated changes, I will try to keep commits focused on one logical change.