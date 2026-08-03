# Git & GitHub Day 05

## Objective

Learn how to inspect changes before committing and compare file versions.

---

# git diff

Shows the exact changes made in files.

```bash
git diff
```

Always run before committing.

---

# git diff --staged

Shows staged changes.

```bash
git diff --staged
```

---

# git status

Shows:

- Modified files
- New files
- Deleted files
- Staged files

```bash
git status
```

---

# git restore

Discard changes in a file.

```bash
git restore filename.py
```

Example

```bash
git restore day05.py
```

Use carefully—this removes uncommitted changes.

---

# git restore --staged

Unstage a file while keeping its changes.

```bash
git restore --staged day05.py
```

---

# Daily Git Workflow

```
Write Code
     ↓
git status
     ↓
git diff
     ↓
git add .
     ↓
git diff --staged
     ↓
git commit
     ↓
git push
```

---

# Commands Practiced

```bash
git status

git diff

git add .

git diff --staged

git commit -m "Day 5: Strings and string manipulation"

git push
```

---

# Best Practices

- Review changes before every commit.
- Commit related changes together.
- Write clear commit messages.
- Keep commits small and meaningful.
- Push only after testing.

---

# Revision Questions

1. What does git diff show?
2. What is the difference between git diff and git diff --staged?
3. What does git restore do?
4. Why should you review changes before committing?
5. What is a good commit message?

---

# Day Status

✅ Git Concepts Learned