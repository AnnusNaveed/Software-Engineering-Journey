''' Bonus Project — Random Password Generator
Note: This introduces Python's random module. We'll study modules in detail later, but this example gives you a practical preview.'''
import random

characters = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*"
)# pool from which random characters are selected.


def generate_password(length):
    password = ""

    for i in range(length):
        password += random.choice(characters) # Each loop, random.choice() picks one random character.
    return password


length = int(input("Enter Password Length: "))

print("Generated Password:", generate_password(length))

'''Complete Execution Flow
User enters:
8
        │
        ▼
length = 8
        │
        ▼
generate_password(8)
        │
        ▼
password = ""
        │
        ▼
Loop runs 8 times
        │
        ▼
Random character selected each time
        │
        ▼
Password grows:

""
 ↓
"A"
 ↓
"A7"
 ↓
"A7#"
 ↓
"A7#k"
 ↓
"A7#kP"
 ↓
"A7#kP9"
 ↓
"A7#kP9!"
 ↓
"A7#kP9!x"
        │
        ▼
return password
        │
        ▼
print()
        │
        ▼
Generated Password: A7#kP9!x
'''