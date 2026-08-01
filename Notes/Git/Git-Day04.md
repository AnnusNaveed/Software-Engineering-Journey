# Git & GitHub Day 04

## Date

01 August 2026

---

# Objective

Learn how to inspect previous commits and understand commit history.

---

# Why is Commit History Important?

Git stores every commit permanently.

You can:

- View previous work.
- Compare versions.
- Restore old code.
- Understand project progress.

---

# git log

Shows complete commit history.

Command

```bash
git log
```

Information shown

- Commit Hash
- Author
- Date
- Commit Message

---

# git log --oneline

Shows a short version.

```bash
git log --oneline
```

Example

```
91c24ab Day 4

478e160 Day 3

244cdfe Day 2
```

---

# git show

Displays detailed information about a specific commit.

Command

```bash
git show COMMIT_HASH
```

Example

```bash
git show 91c24ab
```

---

# git diff

Shows differences between versions.

```bash
git diff
```

Always review your changes before committing.

---

# Git Workflow

```
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

git commit -m "Day 4: Functions and modular programming"

git log --oneline

git show HEAD

git push
```

---

# Best Practices

- Write meaningful commit messages.
- Commit one logical change at a time.
- Review changes before committing.
- Push after successful testing.
- Keep commit history clean.

---

# Revision Questions

1. What does git log do?
2. Difference between git log and git log --oneline?
3. What does git show display?
4. Why is commit history useful?
5. Why should commits be small and meaningful?

---

# Day Status

✅ Git History Concepts Learned