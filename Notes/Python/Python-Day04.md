# Python Day 04 - Functions

## Date

01 August 2026

---

# Objective

Learn how to organize programs into reusable blocks of code using functions.

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, we define it once and call it whenever needed.

---

# Why Use Functions?

Functions help us:

- Reduce code duplication (DRY - Don't Repeat Yourself)
- Improve code readability
- Make debugging easier
- Reuse code
- Break large programs into smaller modules
- Improve maintainability

---

# Real-Life Example

Imagine a coffee machine.

Pressing one button starts many internal steps:

```
Press Button

↓

Grind Coffee

↓

Boil Water

↓

Mix Coffee

↓

Serve Coffee
```

Similarly, in programming:

```python
make_coffee()
```

The function performs all the required steps internally.

---

# Function Syntax

```python
def function_name():
    statements
```

Example

```python
def greet():
    print("Hello")
```

Calling the function

```python
greet()
```

Output

```
Hello
```

---

# Function Definition

A function definition creates the function.

```python
def greet():
    print("Hello")
```

Nothing happens until the function is called.

---

# Function Call

```python
greet()
```

Now the function executes.

---

# Program Flow

```
Program Starts

↓

Function Defined

↓

Nothing Executes

↓

Function Called

↓

Function Executes

↓

Returns to Main Program
```

---

# Parameters

Parameters receive values when the function is called.

Example

```python
def greet(name):
    print("Hello", name)
```

---

# Arguments

Arguments are the actual values passed to a function.

```python
greet("Annus")
```

Parameter

```
name
```

Argument

```
"Annus"
```

---

# Multiple Parameters

```python
def student(name, age):

    print(name)
    print(age)

student("Annus", 22)
```

---

# Return Statement

A function can return a value.

```python
def add(a, b):
    return a + b

answer = add(10, 20)

print(answer)
```

Output

```
30
```

---

# print() vs return

## print()

Displays the result only.

```python
def square(x):
    print(x * x)
```

---

## return

Returns the result for future use.

```python
def square(x):
    return x * x
```

Example

```python
result = square(5)

print(result)
```

---

# Local Variables

Variables declared inside a function.

Example

```python
def demo():

    x = 10

    print(x)
```

Outside

```python
print(x)
```

Output

```
NameError
```

---

# Global Variables

Variables created outside a function.

```python
name = "Annus"

def show():

    print(name)

show()
```

Output

```
Annus
```

---

# Advantages of Functions

- Reusable
- Easy to maintain
- Easy to debug
- Cleaner code
- Modular programming
- Better collaboration

---

# Common Mistakes

❌ Forgetting to call the function.

❌ Wrong indentation.

❌ Forgetting return.

❌ Passing incorrect arguments.

❌ Using local variables outside the function.

---

# Best Practices

- Use meaningful names.
- Keep functions short.
- One function should perform one task.
- Prefer return when values are needed later.
- Add comments only when necessary.

---

# Functions Learned

- def
- return

---

# Keywords Learned

- def
- return

---

# Programs to Build

- Greeting Function
- Calculator Function
- Even/Odd Checker
- Student Result System
- Area Calculator
- Password Generator (Bonus)

---

# Interview Questions

1. What is a function?
2. Why do we use functions?
3. Difference between parameter and argument?
4. Difference between print() and return?
5. Difference between local and global variables?
6. What happens if a function is never called?
7. What is modular programming?

---

# Revision Summary

✅ Function Definition

✅ Function Call

✅ Parameters

✅ Arguments

✅ Return

✅ Local Variables

✅ Global Variables

---

# Day Status

✅ Completed Successfully