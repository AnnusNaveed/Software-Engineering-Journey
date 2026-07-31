# Git & GitHub Day 03

## Date

31 July 2026

---

# Objective

Learn how to inspect repository changes and manage commit history.

---

# Why Check Changes Before Committing?

Before creating a commit, always review:

- What changed?
- Which files changed?
- Is anything missing?
- Is anything accidental?

This prevents unnecessary commits.

---

# git status

Shows the current state of the repository.

Command

```bash
git status
```

Possible Results

- Modified
- Deleted
- New File
- Renamed
- Working tree clean

---

# git diff

Shows the exact differences between the current files and the last commit.

Command

```bash
git diff
```

Use this before every commit.

---

# git add

Moves files to the Staging Area.

Single File

```bash
git add file.py
```

Entire Project

```bash
git add .
```

---

# git commit

Creates a snapshot.

Example

```bash
git commit -m "Day 3: Loops and iteration"
```

---

# git log

Shows commit history.

```bash
git log --oneline
```

Example

```
a52fd3 Day 3

478e160 Day 2

244cdfe Day 1
```

---

# Good Commit Messages

Good

```
Added multiplication table program

Implemented factorial using loops

Completed Day 3 loops
```

Bad

```
update

done

abc
```

---

# Git Workflow

Write Code

↓

git status

↓

git diff

↓

git add .

↓

git commit

↓

git push

---

# Commands Practiced

```bash
git status

git diff

git add .

git commit -m "Day 3: Loops and iteration"

git log --oneline

git push
```

---

# Best Practices

- Commit only working code.
- Review changes before committing.
- Keep commits small.
- Write descriptive commit messages.
- Push after completing a logical task.

---

# Revision Questions

1. What is git diff?
2. Why use git status?
3. Why stage files?
4. What is a commit?
5. How do you see commit history?
6. Why should commits be descriptive?

---

# Day Status

✅ Git Workflow Improved