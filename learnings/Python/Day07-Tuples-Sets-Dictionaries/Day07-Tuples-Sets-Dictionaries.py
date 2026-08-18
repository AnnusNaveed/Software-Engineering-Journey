# Part 1 — Creating a Tuple
student = ("Annus", 22, 3.82)
print(student)

# Part 2 — Accessing Tuple Elements
print(student[0])
print(student[1])
print(student[-1])

# Part 3 — Tuple Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# Part 4 — Tuple Methods
numbers = (10, 20, 30, 20, 40)
print(numbers.count(20))
print(numbers.index(30))

# Part 5 — Tuple Immutability
student = ("Annus", 22)
# student[0] = "Ali" TypeError
student = ("Ali", 22)
print(student)

# Part 6 — Creating Sets   Notice: duplicates are removed.
numbers = {10, 20, 30, 20, 10}
print(numbers)

# Part 7 — add()  Notice: Addition occurs at the start of the set .
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# Part 8 — remove()
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

# Part 9 — discard() Notice: No error occurs if the value is not in the set.
numbers = {10, 20, 30}
numbers.discard(100)
print(numbers)

"""Difference
remove()      |  discard()
Error if      |	No error
value missing | """

# Part 10 — Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference

# Part 11 — Creating Dictionaries
student = {"name": "Annus", "age": 22, "cgpa": 3.82}
print(student)

# Part 12 — Accessing Values
print(student["name"])
print(student.get("age"))

# Part 13 — Difference Between [] and get()

print(student.get("city"))  # Output None
# print(student["city"])  # Output KeyError
# Rule Always prefer
student.get("key")
# when the key might not exist.

# Part 14 — Adding Data
student["city"] = "Lahore"
print(student)

# Part 15 — Updating Data
student["cgpa"] = 3.90
print(student)

# Part 16 — Removing Data
del student["city"]
print(student)

# Part 17 — pop()
removed = student.pop("cgpa")
print(removed)
print(student)

# Part 18 — Dictionary Methods
student = {"name": "Annus", "age": 22, "cgpa": 3.82}

print(student.keys())
print(student.values())
print(student.items())

# Part 19 — Loop Through Dictionary
for key, value in student.items():
    print(key, ":", value)

# Part Union20 — copy()
student = {"name": "Annus", "age": 22}

new_student = student.copy()
print(new_student)

# Part 21 — clear()
student.clear()
print(student)
print(new_student)

# Practice Challenges

# Challenge 1
"""
Create a tuple of your favorite programming languages.
Print every language using a loop."""
favorite = ("Python", "C++", "C", "JavaScript", "Assembly")
for i in favorite:
    print(i)

# Challenge 2
"""
Create two sets.
Print:
Union
Intersection
Difference """
set1 = {1, 2, 3, 4, 5}
set2 = {2, 6, 7, 8, 9}
print("Union =", set1 | set2)
print("Intersection =", set1 & set2)
print("Difference =", set1 - set2)

# Challenge 3 Create a dictionary for yourself.
student = {"name": "Annus", "age": 22, "city": "Lahore", "cgpa": 3.82}
for key, value in student.items():
    print(key, ":", value)

# Challenge 4
"""
Ask the user for:
Name
Age
City
Store them in a dictionary.
Print
----- Student Profile -----
Name :
Age :
City : """

print("----- Student Profile -----")
student = {
    "Name": input("Enter Your Name :").strip().title(),
    "Age": int(input("Enter Your Age:")),
    "City": input("Enter Your City :").strip().title(),
}
print("\n----- Student Profile -----")
print(f"Name : {student['Name']}")
print(f"Age  : {student['Age']}")
print(f"City : {student['City']}")
print("-" * 32)

# Challenge 5 Check whether "cgpa" exists in the dictionary.

if "cgpa" in student:
    print("CGPA exists")
else:
    print("CGPA does not exist")

# Bonus Challenge
"""
Create a dictionary of five subjects.
Print:
Highest Marks
Lowest Marks
Average Marks
Use:
marks.values()"""
marks = {"PF": 90, "OOP": 88, "DSA": 95, "DB": 91, "AI": 87}
values = marks.values()
print(f"Highest Marks ={max(values)}")
print(f"Lowest Marks ={min(values)}")
print(f"Average Marks ={sum(values)/len(marks)}")

# ⭐ Professional Challenge
"""
Build an Employee Record.
Print it in a professional card format.
"""
employee = {
    "id": 101,
    "name": "Ali",
    "department": "Software",
    "salary": 120000,
    "city": "Lahore",
}

print("=" * 30)
print("       Employee Record")
print("=" * 30)

for key, value in employee.items():
    print(f"{key.title():<12}: {value}")

print("=" * 30)