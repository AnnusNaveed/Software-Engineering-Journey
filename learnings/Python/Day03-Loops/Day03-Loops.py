# iF YOU WANT TO print the number five times like:
print("Loops")
print("Loops")
print("Loops")
print("Loops")
print("Loops")
# instead of this loops are used , easier , shorter & iterative
# always start from 0 to n-1

for i in range(5):
    print("Loops")

# While loop
count = 1

while count <= 5:
    print(count)
    count += 1

    # Infinite loop
    # while True:
    print("Hello")

# For loop
for number in range(5):
    print(number)

# Range function
#  I argument
print(list(range(5)))  # [0,1,2,3,4]
# II argument
print(tuple(range(2, 8)))  # (2, 3, 4, 5, 6, 7)
# III argument
print(set(range(3)))
for i in range(2, 20, 2):
    print(i)  # 2, 4, 6, 8, 10, 12, 14, 16, 18

# Loop control statements
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)

# Pass statement
for i in range(5):
    if i == 2:
        pass
    print(i)

# Nested loops
for i in range(3):
    for j in range(2):
        print(i, j)

# Print Even Numbers
count = 2
while count <= 20:
    print(count)
    count += 2

# Countdown
count = 10

while count >= 1:
    print(count)
    count -= 1

print("Blast Off ")

# Range with Start
for i in range(2, 5):
    print(i)

# Reverse Counting
for x in range(50, 0, -2):
    print(x)

# Loop Through a String
for letter in "Python":
    print(letter)

# Sum Using Loop
total = 0
for i in range(1, 6):
    total += i
print("The sum is:", total)

# Multiplication Table
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")

""" Practice Challenge """

#  Print numbers 1–100.
for i in range(1, 101):
    print(i)

# Print odd numbers from 1–50.
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# Print your name 20 times.
Name = "Annus Naveed"
for i in range(20):
    print(Name)

# Print the 10-times table.
num = 10
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Find the sum of numbers from 1 to 100.
total = 0
for i in range(1, 101):
    total += i
print("The sum is:", total)
