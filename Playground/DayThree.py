# Program 1 — Number Counter
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(i)

# Program 2 — Even & Odd Number Generator
N = int(input("Enter a number: "))
print("Even numbers:")
print(0)  # zero is considered even
for i in range(2, N + 1, 2):
    print(i)
print("Odd numbers:")
for i in range(1, N + 1, 2):
    print(i)

# Program 3 — Multiplication Table Generator
input_number = int(input("Enter a number: "))
print(f"Multiplication Table for {input_number}:")
for i in range(1, 11):
    result = input_number * i
    print(f"{input_number} x {i} = {result}")

# Challenge = Modify it to print tables from 1 to 10.
for num in range(1, 11):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")
    print()  # Print a blank line for better readability

# Program 4 — Sum & Average Calculator
number = int(input("Enter ending number: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
average = total_sum / number if number > 0 else 0
print(f"Sum: {total_sum}")
print(f"Average: {average}")

# Program 5 — Factorial Calculator
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is: {factorial}")
