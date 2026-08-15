# Part 1 — Creating Lists
fruits = ["Apple", "Banana", "Orange"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Annus", 22, 3.82, True]

print(fruits)
print(numbers)
print(mixed)

# Part 2 — Accessing Elements (Indexing)
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])

# Part 3 — List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])

# Part 4 — Updating Elements
fruits = ["Apple", "Banana", "Orange"]

fruits[1] = "Mango"
print(fruits)

# Part 5 — append() Adds one item at the end.

fruits = ["Apple", "Banana"]
fruits.append("Orange")

print(fruits)

# Part 6 — insert() Adds an item at a specific position.

fruits = ["Apple", "Orange"]
fruits.insert(1, "Kiwi")

print(fruits)

# Part 7 — extend() Adds multiple items.

fruits = ["Apple"]
fruits.extend(["Banana", "Orange", "Mango"])

print(fruits)

# Difference
numbers = [1, 2]
numbers.append([3, 4])

print(numbers)

numbers = [1, 2]
numbers.extend([3, 4])

print(numbers)

# Part 8 — remove() Removes the first matching value

fruits = ["Banana", "Apple", "Banana", "Orange"]
fruits.remove("Banana")

print(fruits)

# Part 9 — pop() Removes by index.

fruits = ["Apple", "Banana", "Orange", "Kiwi", "Grapes"]
Removed = fruits.pop()
removed = fruits.pop(2)

print(removed)
print(Removed)
print(fruits)

# Part 10 — clear()
numbers = [10, 20, 30]
numbers.clear()

print(numbers)

# Part 11 — sort()
numbers = [40, 10, 30, 20]
numbers.sort()

print(numbers)

# Part 12 — reverse()
numbers = [10, 20, 30]
numbers.reverse()

print(numbers)

# Part 13 — index()
fruits = ["Apple", "Banana", "Orange"]

print(fruits.index("Banana"))

# Part 14 — count()
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# Part 15 — copy()
original = [10, 20, 30]

duplicate = original.copy()
print(original)
print(duplicate)

# Part 16 — Loop Through a List
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

# Part 17 — enumerate() returns th index & value while iterating an iterable
students = ["Ali", "Ahmed", "Sara"]

for index, student in enumerate(students):
    print(index, student)

# Part 18 — Membership Operators
fruits = ["Apple", "Banana", "Orange"]

print("Apple" in fruits)
print("Kiwi" in fruits)
print("Kiwi" not in fruits)

# Part 19 — Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])
print(matrix[2][0])
print(matrix[0][0])

# Part 20 — Useful Built-in Functions
numbers = [10, 20, 30, 40]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


"""Practice Challenges (Do Without Looking)"""
# Challenge 1
"""Create a list of 5 favorite programming languages and print each using a for loop"""

languages = ["python", "c++", "c", "react", "node.js"]
for programming in languages:
    print(programming)

# Challenge 2
"""Ask the user to enter 5 numbers, store them in a list, then print:
Largest number
Smallest number
Sum
Average"""

numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"\nNumbers : {numbers}")
print(f"Largest : {max(numbers)}")
print(f"Smallest: {min(numbers)}")
print(f"Sum     : {sum(numbers)}")
print(f"Average : {sum(numbers) / len(numbers)}")

# Challenge 3
# Create a list of student names and check whether "Annus" exists.

students = ["Ali", "Ahmed", "Annus", "Usman", "Hamza"]

if "Annus" in students:
    print("Annus exists in the list.")
else:
    print("Annus does not exist in the list.")

# Challenge 4
# Sort a list in ascending order and then reverse it to descending order.

numbers = [45, 12, 89, 23, 67, 5]

# Ascending Order
numbers.sort()
print(f"Ascending Order : {numbers}")

# Descending Order
numbers.reverse()
print(f"Descending Order: {numbers}")

numbers.sort(reverse=True)  # another method
print(numbers)


# Challenge 5
# Remove duplicate values using a list.

numbers = [10, 20, 20, 30, 40, 40, 50]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"Original List : {numbers}")
print(f"Unique List   : {unique_numbers}")
unique_numbers = sorted(set(numbers)) #another method
print(unique_numbers)


#Bonus Challenge
'''Create a list of 10 numbers.
Print:
Even numbers
Odd numbers
Total even numbers
Total odd numbers
Example:
Numbers : [1,2,3,4,5,6,7,8,9,10]
Even Numbers : [2,4,6,8,10]
Odd Numbers : [1,3,5,7,9]
Total Even : 5
Total Odd : 5'''
# Bonus Challenge

numbers = []

print("Enter 10 Numbers")

for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("\n" + "=" * 35)
print(f"Numbers      : {numbers}")
print(f"Even Numbers : {even_numbers}")
print(f"Odd Numbers  : {odd_numbers}")
print(f"Total Even   : {len(even_numbers)}")
print(f"Total Odd    : {len(odd_numbers)}")
print("=" * 35)