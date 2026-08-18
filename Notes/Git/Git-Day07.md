# Git & GitHub Day 07

## Objective

Learn how to inspect changes, compare versions, and work with branches.

---

# git branch

Shows all local branches.

```bash
git branch
```

Example

```
* master
```

The * indicates the current branch.

---

# Create a New Branch

```bash
git branch feature-login
```

---

# Switch Branch

```bash
git switch feature-login
```

or

```bash
git checkout feature-login
```

---

# Create and Switch Together

```bash
git switch -c feature-login
```

---

# Why Branches?

```
Main Project
      │
      ├── Login Feature
      │
      ├── Payment Feature
      │
      ├── Dashboard Feature
      │
      └── Bug Fixes
```

Branches allow multiple features to be developed independently.

---

# git diff

Compare uncommitted changes.

```bash
git diff
```

---

# git log --oneline

Compact history.

```bash
git log --oneline
```

---

# git show

View details of a commit.

```bash
git show HEAD
```

---

# Daily Workflow

```
Code

↓

git status

↓

git diff

↓

git add .

↓

git commit

↓

git log --oneline

↓

git push
```

---

# Commands Practiced

```bash
git status

git diff

git add .

git commit -m "Day 7: Tuples, Sets and Dictionaries"

git log --oneline

git branch

git switch -c feature-name

git push
```

---

# Best Practices

✔ Keep main stable.

✔ Create a branch for every feature.

✔ Use meaningful branch names.

✔ Commit small logical changes.

✔ Push regularly.

---

# Interview Questions

1. What is a Git branch?

2. Why do we use branches?

3. Difference between git switch and git checkout?

4. How do you create a new branch?

5. What does git diff do?

---

# Day Status

✅ Git Concepts Learned