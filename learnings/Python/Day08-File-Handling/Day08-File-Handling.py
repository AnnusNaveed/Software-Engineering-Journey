# 1️. Basic File Creation
with open("test.txt", "w") as file:
    file.write("Hello Python!")

# 2️. Write Multiple Lines
with open("languages.txt", "w") as file:
    file.write("Python\n")
    file.write("C++\n")
    file.write("JavaScript\n")
    file.write("Java\n")

# 3️⃣ Read the File
with open("languages.txt", "r") as file:
    content = file.read()
print(content)

# 4️⃣ Read Line by Line
with open("languages.txt", "r") as file:
    for line in file:
        print(
            line.strip()
        )  # Without strip(), the newline character \n can produce unwanted spacing.

# 5️⃣ Append Data
with open("languages.txt", "a") as file:
    file.write("Go\n")

"""Remember
w → Replace
a → Add"""

# 6️⃣ Readlines()
with open("languages.txt", "r") as file:
    languages = [
        line.rstrip("\n") for line in file.readlines()
    ]  # rstrip("\n") removes specifically the newline rather than all surrounding whitespace.F

print(languages)

# 7️⃣ Exception Handling: The program doesn't crash.
try:
    with open("unknown.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The requested file does not exist.")

# 8️⃣ CSV — Writing
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "CGPA"])
    students = [
        ["Annus", 22, 3.82],
        ["Ali", 23, 3.45],
        ["Ahmed", 24, 3.71],
    ]
    writer.writerows(students)


# 9️⃣ CSV — Reading
import csv

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)  # csv.DictReader() when your CSV has headers:

    # Notice: CSV values are read as strings.
    for row in reader:
        for row in reader:
            print(f"Name : {row['Name']}")
            print(f"Age  : {int(row['Age'])}")
            print(f"CGPA : {float(row['CGPA'])}")
            print("-" * 25)

# 🔟 JSON — Writing
import json

student = {"name": "Annus", "age": 22, "department": "BSCS", "cgpa": 3.82}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# 1️⃣1️⃣ JSON — Reading
import json

with open("student.json", "r") as file:
    student = json.load(file)
print(student)
print(student["name"])
print(student["cgpa"])

# 1️⃣2️⃣ JSON + List : JSON isn't limited to one dictionary.
import json

students = [
    {"name": "Annus", "cgpa": 3.82},
    {"name": "Ali", "cgpa": 3.45},
    {"name": "Ahmed", "cgpa": 3.71},
]

with open("students.json", "w") as file:

    json.dump(students, file, indent=4)
"""
List
 ├── Dictionary
 └── Dictionary
 This structure is extremely common when working with APIs and databases."""

"""
Practice Tasks

Don't just copy the examples."""

# Task 1
"""
Create personal.txt.

Store:
Name
Age
University
Degree
City
Then read and display it."""

with open("personal.txt", "w") as file:
    file.write("Name: Muhammad Annus Naveed\n")
    file.write("Age: 22\n")
    file.write("University: Lahore Garrison University\n")
    file.write("Degree: BS Computer Science\n")
    file.write("City: Lahore\n")

with open("personal.txt", "r") as file:
    data = file.read()

print("----- Personal Information -----")
print(data)

"""
Task 2

Create a program that asks:
Enter your note:
and appends it to:
notes.txt
Every execution should add another note."""

note = input("Enter your note: ")
with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully!\n")

"""
Task 3

Create students_append.csv.
Ask the user for:
Name
Age
CGPA
and append the student to the CSV."""

import csv
import os

# Name
while True:
    name = input("Enter Your Name : ").strip().title()

    if name:
        break

    print("Name cannot be empty!")

# Age
while True:
    try:
        age = int(input("Enter Your Age : "))

        if age > 0:
            break

        print("Age must be greater than 0!")

    except ValueError:
        print("Please enter a valid age number!")

# CGPA
while True:
    try:
        cgpa = float(input("Enter Your CGPA : "))

        if 0 <= cgpa <= 4:
            break

        print("CGPA must be between 0 and 4!")

    except ValueError:
        print("Please enter a valid CGPA!")

# CSV File
file_name = "students_append.csv"
file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Name", "Age", "CGPA"])

    writer.writerow([name, age, cgpa])

print("Student added successfully!\n")

"""
Task 4

Create students_dictionary.json.
Ask the user for:
Name
Age
Department
CGPA
Store the student as a dictionary. """

import json

# Name
while True:
    name = input("Enter Your Name :").strip().title()

    if name:
        break

    print("Name cannot be empty!")

# Age
while True:
    try:
        age = int(input("Enter Your Age :"))

        if age > 0:
            break
        print("Age must be greater than 0!")

    except ValueError:
        print("Please enter a valid age number!")


# Department
while True:
    department = input("Enter Your Department :").strip().title()

    if department:
        break

    print("Department cannot be empty!")

# Cgpa
while True:
    try:
        cgpa = float(input("Enter Your CGPA : "))

        if 0 <= cgpa <= 4:
            break

        print("CGPA must be between 0 and 4!")

    except ValueError:
        print("Please enter a valid CGPA!")

student = {"Name": name, "Age": age, "Department": department, "CGPA": cgpa}

with open("students_dictionary.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nStudent information saved successfully!\n")

"""
Challenge:
Student Data Persistence

Your program should:

1. Ask for student information
       ↓
2. Store it in a dictionary
       ↓
3. Save dictionary to JSON
       ↓
4. Read JSON
       ↓
5. Display student information

Expected:
========== Student Profile ==========
Name       : Annus
Age        : 22
Department : BSCS
CGPA       : 3.82
====================================== """

import json

# 1. Ask for student information

# Name
while True:
    name = input("Enter Your Name :").strip().title()

    if name:
        break

    print("Name cannot be empty!")

# Age
while True:
    try:
        age = int(input("Enter Your Age :"))

        if age > 0:
            break
        print("Age must be greater than 0!")

    except ValueError:
        print("Please enter a valid age number!")


# Department
while True:
    department = input("Enter Your Department :").strip().title()

    if department:
        break

    print("Department cannot be empty!")

# Cgpa
while True:
    try:
        cgpa = float(input("Enter Your CGPA : "))

        if 0 <= cgpa <= 4:
            break

        print("CGPA must be between 0 and 4!")

    except ValueError:
        print("Please enter a valid CGPA!")

# 2. Store in dictionary
student = {"Name": name, "Age": age, "Department": department, "CGPA": cgpa}

# 3. Save dictionary to JSON
with open("student_profile.json", "w") as file:
    json.dump(student, file, indent=4)

# 4. Read JSON
with open("student_profile.json", "r") as file:
    student = json.load(file)

# 5. Display student information
print("\n========== Student Profile ==========")
print(f"Name       : {student['Name']}")
print(f"Age        : {student['Age']}")
print(f"Department : {student['Department']}")
print(f"CGPA       : {student['CGPA']}")
print("=====================================")

"""
Important Professional Challenge

Create a JSON file containing multiple students.
Then:
Load the JSON.
Display all students.
Calculate average CGPA.
Find highest CGPA.
Find lowest CGPA.

Concept:

students.json
      ↓
json.load()
      ↓
Python List
      ↓
Dictionaries
      ↓
Processing """

import json

# 1. Load JSON
with open("multiple_students.json", "r") as file:
    students = json.load(file)

# 2. Display all students
print("\n========== All Students ==========\n")
for index, student in enumerate(students, start=1):
    print(f"Student {index}")
    print(f"Name       : {student['Name']}")
    print(f"Age        : {student['Age']}")
    print(f"Department : {student['Department']}")
    print(f"CGPA       : {student['CGPA']}")
    print("-" * 35)

# 3. Calculate average CGPA
cgpas = [student["CGPA"] for student in students]
average = sum(cgpas) / len(cgpas)

# 4. Highest CGPA
highest = max(students, key=lambda student: student["CGPA"])

# 5. Lowest CGPA
lowest = min(students, key=lambda student: student["CGPA"])

print("\n========== Statistics ==========")

print(f"Average CGPA : {average:.2f}")
print(f"Highest CGPA : {highest['Name']}" f"({highest['CGPA']})")
print(f"Lowest CGPA : {lowest['Name']}" f"({lowest['CGPA']})")

print("=" * 35)

"""
max(students) → searches through the students.
key= → tells max() what value to compare.
lambda student: → defines a small temporary function where student represents each dictionary.
student["CGPA"] → gets that student's CGPA.

So it effectively means:

Compare:
Annus  → 3.82
Ali    → 3.45
Ahmed  → 3.71
Sara   → 3.91

Highest → Sara

Flowchart:
                ┌─────────────────────┐
                │   students (List)   │
                └──────────┬──────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │        max()           │
              │ Find the highest value │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │ key = lambda student:  │
              │     student["CGPA"]     │
              └───────────┬────────────┘
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
       ┌─────────┐   ┌─────────┐   ┌─────────┐
       │ Annus   │   │   Ali    │   │  Sara   │
       │ CGPA    │   │  CGPA    │   │  CGPA   │
       │  3.82   │   │  3.45    │   │  3.91   │
       └────┬────┘   └────┬────┘   └────┬────┘
            │             │             │
            ▼             ▼             ▼
          3.82          3.45          3.91
            │             │             │
            └─────────────┼─────────────┘
                          ▼
                 ┌────────────────┐
                 │ Compare values │
                 └───────┬────────┘
                         ▼
                    Highest = 3.91
                         │
                         ▼
                 ┌───────────────┐
                 │ Return Sara's │
                 │ dictionary    │
                 └───────────────┘  
                 
Remember the structure:
max(
    WHAT TO SEARCH,
    key = HOW TO COMPARE
)
"""
