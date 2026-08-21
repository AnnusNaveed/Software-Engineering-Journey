# Program 2 — Even & Odd Number Generator
N = int(input("Enter a number: "))
print("Even numbers:")
print(0)  # zero is considered even
for i in range(2, N + 1, 2):
    print(i)
print("Odd numbers:")
for i in range(1, N + 1, 2):
    print(i)