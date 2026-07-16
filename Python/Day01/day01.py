# reserved keywords check
# import keyword
# print(keyword.kwlist)

"""import math
print(math.ceil(4.2))   # 5  → rounds up
print(math.ceil(7.0))   # 7  → already an integer
print(math.ceil(-2.3))  # -2 → rounds up toward zero
print(math.floor(2.9))"""

# variables & datatypes
name = "Annus"
age = 26
pi = 3.2456
student = True
print(name, age, pi, student)

# input & output
age = input("Enter your age :")
print(age)

# f'strings
age = int(input("enter your age :"))
print(f"""your age is: {age}.
      condition {age>=8}""")

"""
type conversion
"""
# Convert Integer to String
age = 22
text = str(age)
print(age)
# Convert Float to Integer
cgpa = 3.90
print(int(cgpa))

# operators
# Addition
a = 5 + 5
print(a)
# Subtraction
a = 5 - 5
print(a)
# Multiplication
a = 5 * 5
print(a)
# Division always returns the float value
a = 5 / 5
print(a)
# Floor division ~ used for floor values
a = -7 // 2
print(a)
# modulus ` returns reminder` ~ useful in even , odd case
a = 26 % 3
print(a)
# power
a = 2**3
print(a)
