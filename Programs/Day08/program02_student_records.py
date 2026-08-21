# Program 2 — Student Records
"""
Now we'll use JSON.

Objective:
Store multiple student records permanently."""

import json
import os

FILE_NAME = "data/students.json"

os.makedirs("data", exist_ok=True)


def load_students():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Student data file not found. Starting with empty records.")
        return []

    except json.JSONDecodeError:
        print("Student data file contains invalid JSON.")
        return []


def save_students(students):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        print("Student data saved successfully.")

    except OSError as error:
        print(f"File error while saving data: {error}")

    except TypeError as error:
        print(f"Invalid data cannot be converted to JSON: {error}")


def add_student():

    students = load_students()

    name = input("Name: ").strip().title()

    if not name:
        print("Name cannot be empty.")
        return

    while True:
        try:
            age = int(input("Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    department = input("Department: ").strip().title()

    if not department:
        print("Department cannot be empty.")
        return

    while True:
        try:
            cgpa = float(input("CGPA: "))

            if not 0 <= cgpa <= 4:
                print("CGPA must be between 0 and 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid CGPA.")

    student = {"name": name, "age": age, "department": department, "cgpa": cgpa}

    students.append(student)

    save_students(students)


def view_students():

    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n========== STUDENTS ==========")

    for number, student in enumerate(students, start=1):

        try:
            print(f"""
Student #{number}
Name       : {student['name']}
Age        : {student['age']}
Department : {student['department']}
CGPA       : {student['cgpa']}
""")

        except KeyError as error:
            print(f"Student #{number} has missing field: {error}")


add_student()
view_students()

"""
                 PROGRAM
                    │
        ┌───────────┴───────────┐
        │                       │
   USER INPUT              FILE SYSTEM
        │                       │
   ValueError                OSError
        │                       │
        └───────────┬───────────┘
                    │
                  JSON
                    │
             JSONDecodeError
                    │
                    ▼
             DATA STRUCTURE
                    │
                 KeyError
"""