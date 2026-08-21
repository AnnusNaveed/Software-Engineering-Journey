# Program 1 — Student Marks Manager
marks = [87, 91, 79, 95]
students = ["Ali", "Ahmed", "Sara", "Annus"]
print("\n------ Student Marks ------\n")

# zip() combines two lists element by element into pairs.
for student, mark in zip(students, marks):
    print(f"{student:<8} : {mark}")  # left-aligned in a field of 8 characters

print("\nHighest Marks :", max(marks))
print("Lowest Marks  :", min(marks))
print("Average Marks :", sum(marks) / len(marks))