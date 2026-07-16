# Program 1
# Ask for the user's name and age, then print
print("""-----------------
- First Program -
-----------------""")
name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
print(f"Hello, {name}.")
print(f"You are {age} years old.")

# Program 2
"""Build a calculator that takes two numbers and prints:
Addition
Subtraction
Multiplication
Division"""

print("""-----------------
- Second Program -
-----------------""")
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
print(f"Addition is :{a+b}")
print(f"Subtraction is :{a-b}")
print(f"Multiplication is :{a*b}")
if b == 0:
    print("Division by zero is not allowed.")
else:
    print(f"Division is :{a/b}")

    # Program 3
# Ask for three semester CGPAs and calculate the average.
print("""-----------------
- Third Program -
-----------------""")
c = float(input("Ist Sem CGPA :"))
d = float(input("2nd Sem CGPA :"))
e = float(input("3rd Sem CGPA :"))
average = (c + d + e) / 3
print(f"Average CGPA: {average:.2f}")


# Program 4
# Ask for the length and width of a rectangle, then calculate and print the area.
l = float(input("Enter Length :"))
w = float(input("Enter Width :"))
area = l * w
print(f"Area of the rectangle is: {area}")
