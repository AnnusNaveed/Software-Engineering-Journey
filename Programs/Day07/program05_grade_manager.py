# Program 5 — Grade Manager
marks = {"PF": 90, "OOP": 88, "DSA": 95, "DB": 91, "AI": 87}

print("------ Grade Manager ------")
for subject, mark in marks.items():
    print(f"{subject:<8} :{mark}")

average = sum(marks.values()) / len(marks)
print(f"\nHighest :{max(marks.values())}")
print(f"Lowest :{min(marks.values())}")
print(f"Average :{average:.2f}")