# Program 3 — Multiplication Table Generator

# ==========================================
# Part 1 — Single Multiplication Table
# ==========================================
input_number = int(input("Enter a number: "))
print(f"Multiplication Table for {input_number}:")
for i in range(1, 11):
    result = input_number * i
    print(f"{input_number} x {i} = {result}")

# ==========================================
# Part 2 — Challenge: Tables 1 to 10
# ==========================================
for num in range(1, 11):
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")
    print()  # Print a blank line for better readability