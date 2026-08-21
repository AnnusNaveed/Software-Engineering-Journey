# Program 1 — Student Database
"""Objective

Store student information using a dictionary.
Output
========== Student Database ==========
Name        : Annus
Age         : 22
Department  : BS Computer Science
CGPA        : 3.82
City        : Lahore
======================================"""

student = {
    "Name": "Annus",
    "Age": 22,
    "Department": "BS Computer Science",
    "CGPA": 3.42,
    "City": "Lahore",
}

print("=" * 38)
print("      Student Database")
print("=" * 38)

for key, value in student.items():
    print(f"{key:<12}: {value}")
print("=" * 38)