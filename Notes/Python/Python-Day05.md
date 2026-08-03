# Python Day 05 - Strings

## Date

02 August 2026

---

# Objective

Learn how to create, manipulate, search, validate, and format strings in Python.

---

# What is a String?

A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

Examples

```python
name = "Annus"
city = 'Lahore'
course = "Software Engineering"
```

Strings can contain:

- Letters
- Numbers
- Spaces
- Symbols
- Emojis (Unicode)

---

# Why are Strings Important?

Strings are used in almost every software application.

Examples

- Login Systems
- Passwords
- Emails
- Chat Applications
- Search Engines
- AI Chatbots
- File Processing
- APIs
- Web Development

---

# String Indexing

```
Python

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5

 -6 -5 -4 -3 -2 -1
```

Example

```python
text = "Python"

print(text[0])
print(text[3])
print(text[-1])
```

Output

```
P
h
n
```

---

# String Slicing

Syntax

```python
text[start:stop]
```

Example

```python
text = "Python Programming"

print(text[0:6])

print(text[7:18])

print(text[:6])

print(text[7:])
```

Output

```
Python

Programming

Python

Programming
```

Remember

Start → Included

Stop → Excluded

---

# String Length

```python
text = "Python"

print(len(text))
```

Output

```
6
```

---

# String Concatenation

```python
first = "Software"

second = "Engineering"

print(first + " " + second)
```

Output

```
Software Engineering
```

---

# String Repetition

```python
print("=" * 30)
```

Output

```
==============================
```

---

# Membership Operators

```python
text = "Python Programming"

print("Python" in text)

print("Java" not in text)
```

Output

```
True

True
```

---

# Strings are Immutable

Incorrect

```python
name = "Python"

name[0] = "J"
```

Output

```
TypeError
```

Correct

```python
name = "Python"

name = "J" + name[1:]
```

Output

```
Jython
```

---

# Escape Characters

```python
print("He said \"Hello\"")

print("Line1\nLine2")

print("Name\tAge")
```

---

# Raw Strings

```python
path = r"C:\Users\Annus\Documents"
```

Useful for Windows file paths.

---

# Multi-line Strings

```python
message = """
Welcome
to
Python
"""
```

---

# f-Strings

```python
name = "Annus"

cgpa = 3.82

print(f"{name} has CGPA {cgpa}")
```

Output

```
Annus has CGPA 3.82
```

---

# Common String Methods

## upper()

```python
"python".upper()
```

Output

```
PYTHON
```

---

## lower()

```python
"PYTHON".lower()
```

Output

```
python
```

---

## title()

```python
"software engineering".title()
```

Output

```
Software Engineering
```

---

## capitalize()

```python
"python".capitalize()
```

Output

```
Python
```

---

## strip()

Removes spaces.

```python
"  Python  ".strip()
```

---

## replace()

```python
"Python".replace("Python","Java")
```

Output

```
Java
```

---

## find()

```python
"Python".find("t")
```

Output

```
2
```

---

## count()

```python
"banana".count("a")
```

Output

```
3
```

---

## split()

```python
"Python Java C++".split()
```

Output

```
['Python', 'Java', 'C++']
```

---

## join()

```python
"-".join(["A","B","C"])
```

Output

```
A-B-C
```

---

## startswith()

```python
"Python".startswith("Py")
```

Output

```
True
```

---

## endswith()

```python
"Python".endswith("on")
```

Output

```
True
```

---

## isalpha()

Checks whether all characters are letters.

---

## isdigit()

Checks whether all characters are digits.

---

## isalnum()

Checks whether the string contains only letters and numbers.

---

# Best Practices

- Use meaningful variable names.
- Prefer f-strings over '+' for formatting.
- Use strip() before validating user input.
- Avoid unnecessary string concatenation inside loops.
- Choose descriptive method names.

---

# Common Mistakes

❌ Index out of range.

❌ Forgetting strings are immutable.

❌ Confusing find() with index().

❌ Using '+' instead of f-strings everywhere.

---

# Programs Today

- String Basics
- Palindrome Checker
- Password Validator
- Email Validator
- Text Analyzer
- Username Generator

---

# Interview Questions

1. What is a string?
2. What is indexing?
3. What is slicing?
4. Difference between upper() and lower()?
5. What does strip() do?
6. Difference between find() and count()?
7. What are immutable objects?
8. What is an f-string?
9. Difference between split() and join()?
10. What is the use of startswith()?

---

# Revision Summary

✅ String Creation

✅ Indexing

✅ Slicing

✅ Common Methods

✅ Escape Characters

✅ Raw Strings

✅ f-Strings

---

# Day Status

✅ Completed Successfully