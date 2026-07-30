# Python Day 02 - Control Flow

## Date

30 July 2026

---

# Objective

Learn how Python makes decisions using conditions.

---

# What is Control Flow?

Control Flow is the order in which a program executes instructions.

Without control flow:

Program executes line by line.

With control flow:

The program can make decisions.

Example:

```
If it is raining
    Take an umbrella
Else
    Go outside
```

---

# Boolean Data Type

A Boolean has only two values.

```python
True
False
```

Example

```python
print(5 > 3)
```

Output

```
True
```

---

# Comparison Operators

| Operator | Meaning |
|-----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example

```python
age = 20

print(age >= 18)
```

Output

```
True
```

---

# Logical Operators

## and

Returns True only if both conditions are True.

```python
age = 20
cgpa = 3.4

print(age >= 18 and cgpa >= 3)
```

---

## or

Returns True if at least one condition is True.

```python
print(age >= 18 or cgpa >= 3)
```

---

## not

Reverses the Boolean value.

```python
print(not True)
```

Output

```
False
```

---

# if Statement

Syntax

```python
if condition:
    statement
```

Example

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# if else

```python
if condition:
    statement
else:
    statement
```

Example

```python
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

# if elif else

Used when multiple conditions exist.

Example

```python
marks = 82

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("Fail")
```

---

# Nested if

An if statement inside another if statement.

Example

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
```

---

# Truthy and Falsy Values

Falsy values:

```
0
0.0
False
None
""
[]
{}
set()
```

Everything else is considered Truthy.

---

# Indentation

Python uses indentation instead of braces.

Correct

```python
if age >= 18:
    print("Adult")
```

Wrong

```python
if age >= 18:
print("Adult")
```

---

# Common Mistakes

- Using = instead of ==
- Incorrect indentation
- Forgetting :
- Comparing strings with integers
- Writing multiple unrelated if statements instead of elif

---

# Best Practices

- Keep conditions simple.
- Use meaningful variable names.
- Avoid deep nesting.
- Use elif instead of multiple if statements when appropriate.

---

# Functions Learned

- input()
- print()
- bool()

---

# Programs Completed

- Age Checker
- Positive/Negative/Zero
- Grade Calculator
- Login System
- Largest Number
- Number Guess (Bonus)

---

# Revision Questions

1. What is Control Flow?
2. What is a Boolean?
3. Difference between == and = ?
4. Difference between if and elif?
5. When should Nested if be used?
6. Difference between and and or?
7. What does not do?
8. What are Truthy and Falsy values?

---

# Day Status

✅ Completed Successfully