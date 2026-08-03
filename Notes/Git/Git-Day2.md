# Git & GitHub Day 02

## Date

30 July 2026

---

# Objective

Learn how Git tracks changes after the repository has been created.

---

# Git Workflow

```
Modify Code

↓

git status

↓

git add

↓

git commit

↓

git push

↓

GitHub
```

---

# git status

Shows the current state of the repository.

Command

```bash
git status
```

Possible outputs

- Modified files
- New files
- Deleted files
- Nothing to commit

---

# git add

Moves changes to the Staging Area.

Single file

```bash
git add file.py
```

All files

```bash
git add .
```

---

# What is the Staging Area?

Think of it as a waiting room.

```
Modified File

↓

Staging Area

↓

Commit
```

Git asks:

"Do you really want to save these changes?"

---

# git commit

Creates a snapshot of your project.

Example

```bash
git commit -m "Day 2: Control Flow"
```

Good commit messages should describe what changed.

---

# git push

Uploads commits to GitHub.

```bash
git push
```

---

# git log

Shows commit history.

```bash
git log --oneline
```

Example

```
478e160 Day 2

244cdfe Day 1
```

---

# git diff

Shows what has changed before committing.

```bash
git diff
```

Use this command before every commit.

---

# Git File Lifecycle

```
Create File

↓

Modified

↓

git add

↓

Staged

↓

git commit

↓

Committed

↓

git push

↓

GitHub
```

---

# Commands Learned

```bash
git status

git add .

git diff

git commit -m "message"

git log --oneline

git push
```

---

# Best Practices

- Check git status before committing.
- Review changes using git diff.
- Commit small logical changes.
- Write meaningful commit messages.
- Push after completing a task.

---

# Today's Git Practice

```bash
git status

git diff

git add .

git status

git commit -m "Day 2: Control flow and conditional statements"

git log --oneline

git push
```

---

# Revision Questions

1. What is the staging area?
2. What is git status used for?
3. What is the purpose of git add?
4. Why do we commit?
5. What does git push do?
6. What does git log show?
7. What does git diff show?

---

# Day Status

✅ Git Workflow Practiced Successfully