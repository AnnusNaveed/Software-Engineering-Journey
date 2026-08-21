def line():
    print("-" * 34)


# Program 3 — Student Result System
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A+"
    elif marks >= 80 and marks < 90:
        return "A"
    elif marks >= 70 and marks < 80:
        return "B"
    elif marks >= 60 and marks < 70:
        return "C"
    elif marks >= 50 and marks < 60:
        return "D"
    elif marks >= 0 and marks < 50:
        return "F"
    else:
        return "Invalid marks. Please enter a value between 0 and 100."


line()
print("Program 3 — Student Result System")
line()
student_name = input("Enter the student's name: ")
marks = float(input("Enter the student's marks (0-100): "))
grade = calculate_grade(marks)

print("\n----- Result -----")
print("Student Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print(
    "Pass / Fail:",
    (
        "Pass"
        if marks >= 50 and marks in [50, 100]
        else (
            "Fail"
            if marks < 50 and marks in [0, 49]
            else "Invalid marks. Please enter a value between 0 and 100."
        )
    ),
)
(
    print("Percentage:", marks, "%")
    if marks in [0, 100]
    else print("Percentage: Invalid marks. Please enter a value between 0 and 100.")
)
print(
    "Remarks:",
    (
        "Excellent"
        if grade in ["A+", "A"]
        else (
            "Good"
            if grade == "B"
            else (
                "Average"
                if grade == "C"
                else "Needs Improvement" if grade == "D" else "Fail"
            )
        )
    ),
)