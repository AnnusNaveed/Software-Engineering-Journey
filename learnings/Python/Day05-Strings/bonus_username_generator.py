# Bonus Project — Username Generator
print("=" * 40)
print("Professional Username Generator")
print("=" * 40)

while True:

    name = input("Enter Full Name: ").strip()

    # Empty input
    if name == "":
        print("Name cannot be empty.\n")
        continue

    # Numbers not allowed
    if any(character.isdigit() for character in name):
        print("Name cannot contain numbers.\n")
        continue

    # Special characters not allowed
    invalid = False

    for character in name:
        if not (character.isalpha() or character.isspace()):
            invalid = True
            break

    if invalid:
        print("Name cannot contain special characters.\n")
        continue

    # Remove extra spaces
    name = " ".join(name.split())

    # Generate username
    username = name.lower().replace(" ", "_") 
    print("_" * 32)
    print("\tGenerated Username")
    print("_" * 32)
    print(username)
    break
