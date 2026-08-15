# Python Day 06 - Lists

## Objective

Learn how to create, access, modify, search, and manage data using Python Lists.

---

# What is a List?

A list is an ordered, mutable collection that can store multiple values.

Example

```python
fruits = ["Apple", "Banana", "Orange"]
```

Lists can store:

- Strings
- Integers
- Floats
- Boolean values
- Other Lists
- Mixed Data Types

---

# Why Use Lists?

Instead of

```python
student1 = "Ali"
student2 = "Ahmed"
student3 = "Sara"
```

Use

```python
students = ["Ali", "Ahmed", "Sara"]
```

Advantages

- Cleaner Code
- Easy Looping
- Easy Searching
- Easy Updating
- Dynamic Size

---

# List Visualization

```
fruits = ["Apple", "Banana", "Orange"]

+---------+---------+---------+
| Apple   | Banana  | Orange  |
+---------+---------+---------+
     0         1         2

    -3        -2        -1
```

---

# Indexing

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])

print(fruits[-1])
```

Output

```
Apple

Orange
```

---

# Slicing

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])

print(numbers[:3])

print(numbers[2:])
```

Output

```
[20,30,40]

[10,20,30]

[30,40,50]
```

Rule

Start → Included

Stop → Excluded

---

# Lists are Mutable

```python
fruits = ["Apple","Banana"]

fruits[0] = "Mango"

print(fruits)
```

Output

```
['Mango', 'Banana']
```

---

# Length

```python
len(fruits)
```

Returns the number of elements.

---

# Membership Operators

```python
"Apple" in fruits

"Kiwi" not in fruits
```

---

# Common List Methods

## append()

Adds an item at the end.

```python
fruits.append("Mango")
```

---

## insert()

Adds an item at a specific index.

```python
fruits.insert(1, "Grapes")
```

---

## extend()

Adds multiple items.

```python
fruits.extend(["Kiwi", "Peach"])
```

---

## remove()

Removes the first matching item.

```python
fruits.remove("Apple")
```

---

## pop()

Removes an item by index.

```python
fruits.pop()

fruits.pop(2)
```

---

## clear()

Removes all items.

```python
fruits.clear()
```

---

## sort()

Sorts the list.

```python
numbers.sort()
```

---

## reverse()

Reverses the list.

```python
numbers.reverse()
```

---

## index()

Returns the index of an item.

```python
fruits.index("Banana")
```

---

## count()

Counts occurrences.

```python
numbers.count(10)
```

---

## copy()

Creates a shallow copy.

```python
new_list = fruits.copy()
```

---

# Loop Through a List

```python
for fruit in fruits:

    print(fruit)
```

---

# Nested Lists

```python
matrix = [

    [1,2,3],

    [4,5,6],

    [7,8,9]

]
```

Access

```python
matrix[1][2]
```

Output

```
6
```

---

# Best Practices

✅ Use meaningful list names.

✅ Store related data together.

✅ Prefer loops over repetitive code.

✅ Avoid modifying a list while iterating over it.

✅ Use append() for adding one item.

---

# Common Mistakes

❌ Accessing an invalid index.

❌ Confusing append() and extend().

❌ Using remove() for an item that doesn't exist.

❌ Forgetting that lists are mutable.

---

# Programs Today

- Student Marks Manager
- Shopping Cart
- To-Do List
- Contact Book
- Expense Tracker
- Inventory Manager

---

# Interview Questions

1. What is a list?

2. Why are lists mutable?

3. Difference between append() and extend()?

4. Difference between remove() and pop()?

5. Difference between sort() and reverse()?

6. What does index() do?

7. What does count() do?

8. What is a nested list?

9. Difference between list and tuple?

10. When should you use a list?

---

# Revision Summary

✅ Creating Lists

✅ Indexing

✅ Slicing

✅ Mutability

✅ Looping

✅ List Methods

✅ Nested Lists

---

# Day Status

✅ Completed Successfully