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