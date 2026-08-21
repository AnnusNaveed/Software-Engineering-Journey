# Program 4 — Sum & Average Calculator
number = int(input("Enter ending number: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
average = total_sum / number if number > 0 else 0
print(f"Sum: {total_sum}")
print(f"Average: {average}")