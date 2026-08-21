# Program 3 — To-Do List
"""Output
Today's Tasks
1. Study Python
2. Complete Assignment
3. Exercise
4. Git Commit"""
tasks = ["Study Python", "Complete Assignment", "Exercise", "Git Commit"]

print("\n------ Today's Tasks ------\n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Challenge Ask the user to enter 5 tasks.
for i in range(5):
    Tasks = input(f"Enter Task {i+1}: ")
    tasks.append(Tasks)

print("\n------ Updated To-Do List ------\n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")