# Python Day 08 — File Handling, CSV & JSON

## Objective

Learn how Python programs permanently store and retrieve data using:

- Text files
- File modes
- File paths
- Exception handling
- CSV
- JSON

---

# 1. Why File Handling?

Variables only exist while the program is running.

```python
name = "Annus"
```

When the program terminates, the variable is gone.

Files provide persistent storage:

```text
Python Program
      ↓
   Write Data
      ↓
     File
      ↓
Program Closes
      ↓
Data Still Exists
```

---

# 2. Opening a File

Basic syntax:

```python
open(filename, mode)
```

Example:

```python
file = open("data.txt", "r")
```

---

# 3. File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read |
| `w` | Write / overwrite |
| `a` | Append |
| `x` | Create a new file |
| `b` | Binary mode |
| `t` | Text mode |

Examples:

```python
open("data.txt", "r")
open("data.txt", "w")
open("data.txt", "a")
```

---

# 4. Read Mode — `r`

Reads an existing file.

```python
with open("data.txt", "r") as file:
    data = file.read()

print(data)
```

If the file doesn't exist, Python raises:

```text
FileNotFoundError
```

---

# 5. Write Mode — `w`

Writes data to a file.

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

Important:

`w` overwrites existing content.

```text
Old Content
     ↓
    "w"
     ↓
New Content
```

---

# 6. Append Mode — `a`

Adds content to the end.

```python
with open("data.txt", "a") as file:
    file.write("\nNew line")
```

Existing content remains.

```text
Old Content
     +
New Content
```

---

# 7. Create Mode — `x`

Creates a new file.

```python
with open("new_file.txt", "x") as file:
    file.write("Created successfully")
```

If the file already exists, Python raises:

```text
FileExistsError
```

---

# 8. Why `with open()`?

Professional approach:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The `with` statement automatically handles closing the file.

Less preferred:

```python
file = open("data.txt", "r")

data = file.read()

file.close()
```

Use:

```python
with open(...)
```

whenever possible.

---

# 9. Reading Methods

## read()

Reads the complete file.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

---

## readline()

Reads one line.

```python
with open("data.txt", "r") as file:
    line = file.readline()
```

---

## readlines()

Reads all lines into a list.

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
```

Example:

```text
[
    "Python\n",
    "Java\n",
    "C++\n"
]
```

---

# 10. Loop Through a File

```python
with open("data.txt", "r") as file:

    for line in file:
        print(line.strip())
```

`strip()` removes unnecessary whitespace and newline characters.

---

# 11. Writing Multiple Lines

```python
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w") as file:
    file.writelines(lines)
```

---

# 12. File Paths

## Relative Path

```python
"data.txt"
```

Means the file is relative to the current working directory.

## Folder Path

```python
"data/students.txt"
```

## Absolute Path

Example:

```text
X:\Software-Engineering-Journey\data\students.txt
```

For projects and GitHub repositories, relative paths are generally preferable.

---

# 13. Checking File Existence

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")
```

---

# 14. Exception Handling

File operations can fail.

Example:

```python
try:

    with open("missing.txt", "r") as file:
        data = file.read()

except FileNotFoundError:

    print("File not found.")
```

---

# 15. CSV

CSV means:

**Comma-Separated Values**

Example:

```text
Name,Age,CGPA
Ali,22,3.4
Ahmed,21,3.7
Sara,22,3.9
```

CSV is useful for:

- Spreadsheet data
- Tabular data
- Reports
- Dataset exchange
- Data analysis

---

# 16. Writing CSV

Python provides the `csv` module.

```python
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "CGPA"])

    writer.writerow(["Annus", 22, 3.82])
```

---

# 17. Reading CSV

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# 18. JSON

JSON means:

**JavaScript Object Notation**

Example:

```json
{
    "name": "Annus",
    "age": 22,
    "cgpa": 3.82
}
```

JSON represents structured data using:

- Objects
- Arrays
- Strings
- Numbers
- Boolean values
- null

---

# 19. Python Dictionary → JSON

Python:

```python
student = {
    "name": "Annus",
    "age": 22,
    "cgpa": 3.82
}
```

Save as JSON:

```python
import json

with open("student.json", "w") as file:

    json.dump(student, file, indent=4)
```

---

# 20. Meaning of `indent=4`

```python
json.dump(student, file, indent=4)
```

`indent=4` formats the JSON with four spaces of indentation, making it easier for humans to read.

It does not change the underlying data.

---

# 21. JSON → Python

```python
import json

with open("student.json", "r") as file:

    student = json.load(file)

print(student)
```

The JSON object becomes a Python dictionary.

---

# 22. dump vs dumps

## dump()

Writes JSON to a file.

```python
json.dump(data, file)
```

## dumps()

Converts Python data to a JSON string.

```python
json_data = json.dumps(data)
```

---

# 23. load vs loads

## load()

Reads JSON from a file.

```python
data = json.load(file)
```

## loads()

Reads JSON from a string.

```python
data = json.loads(json_string)
```

---

# 24. Important JSON Relationship

```text
Python Object
     ↓
json.dump()
     ↓
JSON File
     ↓
json.load()
     ↓
Python Object
```

For strings:

```text
Python Object
     ↓
json.dumps()
     ↓
JSON String
     ↓
json.loads()
     ↓
Python Object
```

---

# 25. JSON in Web Development

This is extremely important.

```text
Frontend
   ↓
HTTP Request
   ↓
JSON
   ↓
Backend API
   ↓
Python
   ↓
Database
```

Example API response:

```json
{
    "id": 101,
    "name": "Annus",
    "cgpa": 3.82
}
```

Future React frontend can receive this data and display it.

---

# 26. CSV vs JSON

| CSV | JSON |
|-----|------|
| Tabular | Structured |
| Rows and columns | Key-value / nested structures |
| Great for spreadsheets | Great for APIs |
| Simple datasets | Complex application data |
| Common in data analysis | Common in web development |

---

# 27. File Handling Best Practices

### Prefer

```python
with open(...)
```

### Use appropriate modes

```text
r → read
w → overwrite
a → append
x → create
```

### Use exception handling

```python
try:
    ...
except FileNotFoundError:
    ...
```

### Prefer relative paths in repositories

Avoid hardcoding:

```text
X:\Users\...\project\...
```

---

# 28. Common Errors

## FileNotFoundError

File doesn't exist.

---

## FileExistsError

Usually occurs with `x` when the file already exists.

---

## PermissionError

Python doesn't have permission to access the file.

---

## IsADirectoryError

A directory was provided where a file was expected.

---

# 29. Quick Revision

```text
open()
   ↓
r → Read
w → Write/Overwrite
a → Append
x → Create
```

```text
read()
readline()
readlines()
write()
writelines()
```

```text
CSV
 ↓
csv.reader()
csv.writer()
```

```text
JSON
 ↓
json.dump()
json.load()
json.dumps()
json.loads()
```

---

# 30. Day 8 Key Takeaways

✅ Files provide persistent storage.

✅ `with open()` is the preferred approach.

✅ `w` overwrites.

✅ `a` appends.

✅ CSV is useful for tabular data.

✅ JSON is useful for structured application data.

✅ `json.dump()` writes JSON to a file.

✅ `json.load()` reads JSON from a file.

✅ `json.dumps()` creates a JSON string.

✅ `json.loads()` parses a JSON string.

✅ JSON is fundamental to REST APIs.

---

