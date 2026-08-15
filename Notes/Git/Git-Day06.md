# Git & GitHub Day 06

## Objective

Learn how to inspect commit history and compare versions.

---

# git log

Shows commit history.

```bash
git log
```

---

# git log --oneline

Compact commit history.

```bash
git log --oneline
```

Example

```
a72be51 Day 6: Lists

9f83aa1 Day 5: Strings

43fe11b Day 4: Functions
```

---

# git show

Displays details of a specific commit.

```bash
git show HEAD
```

or

```bash
git show <commit_hash>
```

---

# git show HEAD

Shows:

- Commit message
- Author
- Date
- Exact code changes

---

# git diff HEAD~1

Compare the latest commit with the previous one.

```bash
git diff HEAD~1
```

---

# git status

Always check before committing.

```bash
git status
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

git commit -m "Day 6: Python Lists"

git log --oneline

git show HEAD

git push
```

---

# Best Practices

- Commit frequently.
- Review history often.
- Use meaningful commit messages.
- Verify commits before pushing.
- Keep one logical change per commit.

---

# Revision Questions

1. What does git log do?

2. Why use --oneline?

3. What does git show display?

4. How do you compare commits?

5. Why should commits be small?

---

# Day Status

✅ Git Concepts Learned