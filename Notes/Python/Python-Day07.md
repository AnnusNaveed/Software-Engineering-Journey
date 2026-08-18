# Python Day 07 - Tuples, Sets & Dictionaries

## Objective

Learn Python's three major collection types and understand when to use each one.

---

# Python Collections

| Collection | Ordered | Mutable | Duplicate Values | Syntax |
|------------|:-------:|:-------:|:----------------:|--------|
| List | Yes | Yes | Yes | [] |
| Tuple | Yes | No | Yes | () |
| Set | No | Yes | No | {} |
| Dictionary | Yes | Yes | Keys: No | {key:value} |

---

# Tuple

A tuple is an ordered but immutable collection.

Example

```python
student = ("Annus", 22, 3.82)
```

Once created, tuple values cannot be modified.

Good Uses

- GPS Coordinates
- RGB Colors
- Months
- Days of Week
- Database Records

Advantages

✔ Faster than lists

✔ Safer (cannot be modified accidentally)

✔ Hashable (usable as dictionary keys)

---

# Accessing Tuple Elements

```python
student = ("Annus",22,3.82)

print(student[0])

print(student[-1])
```

---

# Tuple Methods

```python
count()

index()
```

Example

```python
numbers = (10,20,10,30)

print(numbers.count(10))

print(numbers.index(30))
```

---

# Set

A set is an unordered collection of unique values.

Example

```python
numbers = {10,20,30,20,10}

print(numbers)
```

Output

```
{10,20,30}
```

Duplicate values are removed automatically.

---

# Set Operations

## add()

```python
numbers.add(40)
```

---

## remove()

```python
numbers.remove(20)
```

---

## discard()

Safer than remove() because it doesn't raise an error if the value doesn't exist.

```python
numbers.discard(100)
```

---

## clear()

Removes all values.

---

## union()

```python
A | B
```

or

```python
A.union(B)
```

---

## intersection()

```python
A & B
```

---

## difference()

```python
A - B
```

---

# Dictionary

A dictionary stores data as key-value pairs.

Example

```python
student = {

    "name":"Annus",

    "age":22,

    "cgpa":3.82

}
```

---

# Access Values

```python
student["name"]
```

or

```python
student.get("name")
```

---

# Add Data

```python
student["city"] = "Lahore"
```

---

# Update Data

```python
student["age"] = 23
```

---

# Delete Data

```python
del student["city"]
```

or

```python
student.pop("city")
```

---

# Dictionary Methods

keys()

values()

items()

get()

pop()

update()

clear()

copy()

---

# Loop Through Dictionary

```python
for key, value in student.items():

    print(key, value)
```

---

# Dictionary Visualization

```
+-----------+-----------+
| name      | Annus     |
| age       | 22        |
| cgpa      | 3.82      |
+-----------+-----------+
```

---

# Choosing the Right Collection

Need editable ordered data?

→ List

Need fixed data?

→ Tuple

Need unique values?

→ Set

Need key-value data?

→ Dictionary

---

# Common Mistakes

❌ Using a list when a dictionary is better.

❌ Trying to modify a tuple.

❌ Assuming sets preserve order.

❌ Accessing a missing dictionary key using [].

Use

```python
student.get("name")
```

instead of

```python
student["name"]
```

when the key may not exist.

---

# Best Practices

✔ Use meaningful keys.

✔ Use tuples for constant values.

✔ Use sets to remove duplicates.

✔ Use dictionaries for real-world objects.

✔ Keep keys consistent.

---

# Programs Today

• Student Database

• Phone Book

• Product Catalog

• Bank Account Manager

• Grade Manager

• Warehouse Lookup

---

# Interview Questions

1. What is the difference between List and Tuple?

2. Why are tuples immutable?

3. What is a Set?

4. Why do sets remove duplicates?

5. Difference between remove() and discard()?

6. What is a Dictionary?

7. Difference between get() and []?

8. What does items() return?

9. What are dictionary keys?

10. Which collection would you choose for:

- Student Record
- Shopping Cart
- Unique Emails
- GPS Coordinates

---

# Revision Summary

✅ Tuples

✅ Sets

✅ Dictionaries

✅ Dictionary Methods

✅ Set Operations

✅ Key-Value Pairs

✅ Choosing Correct Collection

---

# Day Status

✅ Completed Successfully