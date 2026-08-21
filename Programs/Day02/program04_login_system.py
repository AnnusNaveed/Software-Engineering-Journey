# Program 4 — Login System
username = str(input("Enter username: "))
password = int(input("Enter password: "))
if username == "admin":
    if password == 1234:
        print("Login successful.")
    else:
        print("Incorrect credentials.")
