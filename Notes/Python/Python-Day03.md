# Python Day 03 - Loops

## Date

31 July 2026

---

# Objective

Learn how to execute a block of code repeatedly using loops.

---

# What is a Loop?

A loop is a programming structure that repeats a block of code until a condition becomes False or until all items have been processed.

Instead of writing the same statement multiple times, a loop performs the repetition automatically.

Example

Without Loop

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

With Loop

```python
for i in range(5):
    print("Hello")
```

---

# Why Do We Use Loops?

- Reduce repetitive code.
- Automate repetitive tasks.
- Process collections of data.
- Improve readability.
- Save development time.

---

# Types of Loops in Python

Python provides two main loops.

1. while Loop
2. for Loop

---

# while Loop

The while loop executes as long as the condition remains True.

Syntax

```python
while condition:
    statements
```

Flow

Condition

↓

True

↓

Execute Statements

↓

Condition Again

↓

False

↓

Stop

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# Infinite Loop

An infinite loop never ends because the condition never becomes False.

Example

```python
while True:
    print("Running...")
```

Stop it using

```
Ctrl + C
```

---

# for Loop

The for loop is used when the number of iterations is known.

Syntax

```python
for variable in iterable:
    statements
```

Example

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# range()

The range() function generates a sequence of numbers.

## One Argument

```python
range(5)
```

Output

```
0 1 2 3 4
```

---

## Two Arguments

```python
range(2,7)
```

Output

```
2 3 4 5 6
```

---

## Three Arguments

```python
range(2,20,2)
```

Output

```
2
4
6
8
10
12
14
16
18
```

---

# Loop Control Statements

## break

Terminates the loop immediately.

Example

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

## continue

Skips the current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output

```
0
1
3
4
```

---

## pass

Acts as a placeholder.

```python
for i in range(5):
    pass
```

---

# Nested Loops

A loop inside another loop.

Example

```python
for i in range(3):

    for j in range(2):

        print(i,j)
```

Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# Common Mistakes

- Forgetting to update the counter in a while loop.
- Wrong indentation.
- Confusing break with continue.
- Incorrect use of range().
- Creating infinite loops accidentally.

---

# Best Practices

- Use for loops when the number of iterations is known.
- Use while loops when the stopping condition is unknown.
- Avoid unnecessary nested loops.
- Use meaningful variable names.
- Keep loop bodies simple.

---

# Functions Learned

- range()

---

# Keywords Learned

- while
- for
- break
- continue
- pass

---

# Programs to Build

- Number Counter
- Even Number Printer
- Multiplication Table
- Sum of Numbers
- Factorial
- Guessing Game (Bonus)

---

# Interview Questions

1. What is a loop?
2. Difference between for and while?
3. What is an infinite loop?
4. Difference between break and continue?
5. What does pass do?
6. Explain range().
7. What is a nested loop?

---

# Revision Summary

✅ while Loop

✅ for Loop

✅ range()

✅ break

✅ continue

✅ pass

✅ Nested Loops

---

# Day Status

✅ Completed Successfully