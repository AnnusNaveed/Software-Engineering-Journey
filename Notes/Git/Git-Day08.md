# Git & GitHub Day 08 — File Handling Project Workflow

## Objective

Learn how to manage file-based project changes correctly with Git.

---

# 1. Why Git Matters for File-Based Projects

Day 8 introduces files such as:

```text
.txt
.csv
.json
```

These become part of the project.

Git tracks changes to these files so you can:

- Review changes
- Restore previous versions
- Collaborate
- Maintain project history

---

# 2. Check Repository Status

```bash
git status
```

This shows:

- Current branch
- Modified files
- Untracked files
- Staged files

---

# 3. View Changes

```bash
git diff
```

Shows changes that haven't been staged.

---

# 4. Stage Files

```bash
git add .
```

This stages changes in the repository.

---

# 5. Review Staged Changes

```bash
git diff --staged
```

Review what will be included in the next commit.

---

# 6. Commit

```bash
git commit -m "Day 8: File handling, CSV and JSON"
```

A commit creates a snapshot of the staged changes.

---

# 7. Push

```bash
git push
```

Uploads local commits to the remote repository.

---

# 8. View History

```bash
git log --oneline
```

Example:

```text
abc1234 Day 8: File handling, CSV and JSON
def5678 Day 7: Tuples, Sets, Dictionaries and mini projects
```

---

# 9. Inspect a Commit

```bash
git show HEAD
```

Shows the changes included in the latest commit.

---

# 10. Complete Daily Workflow

```text
Write Code
    ↓
Create / Modify Files
    ↓
git status
    ↓
git diff
    ↓
git add .
    ↓
git diff --staged
    ↓
git commit -m "..."
    ↓
git push
    ↓
git log --oneline
```

---

# 11. What Should Be Committed?

Commit:

```text
.py files
.md notes
.txt examples
.csv examples
.json examples
```

Do not commit:

```text
passwords
API keys
secret credentials
virtual environments
large generated files
```

---

# 12. Important Security Rule

Never put secrets inside Git.

Bad:

```python
API_KEY = "my-secret-key"
```

Better:

```python
API_KEY = os.getenv("API_KEY")
```

Secrets should eventually be managed through environment variables or secret-management systems.

---

# 13. .gitignore

Your repository should contain a `.gitignore`.

Example:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
```

This prevents unnecessary or sensitive files from being tracked.

---

# 14. Why JSON Files Need Care

JSON files may contain application data.

Example:

```json
{
    "username": "Annus",
    "password": "123456"
}
```

Never commit real passwords or sensitive credentials.

For learning, use fake data.

---

# 15. Git Best Practices

✔ Make focused commits.

✔ Use meaningful commit messages.

✔ Review changes before committing.

✔ Never commit secrets.

✔ Push completed work regularly.

✔ Keep the main branch stable.

---

# 16. Day 8 Git Commands

```bash
git status

git diff

git add .

git diff --staged

git commit -m "Day 8: File handling, CSV and JSON"

git push

git log --oneline
```

---
