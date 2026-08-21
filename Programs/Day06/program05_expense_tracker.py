# Program 5 — Expense Tracker
"""Output
Expenses
Food      : 500
Travel    : 1200
Internet  : 2000
Books     : 800
Total Expense : 4500"""
expenses = [500, 1200, 2000, 800]
categories = ["Food", "Travel", "Internet", "Books"]
print("\n------ Expense Tracker ------\n")
for category,expense in zip(categories,expenses):
    print(f"{category:<10}{expense}")
print("\nTotal Expense :",sum(expenses))
#Challenge

'''Calculate
Highest expense
Lowest expense
Average expense'''
print("\nHighest Expense :",max(expenses))
print("\nLowest Expense :",min(expenses))
print("\nAverage Expense :",sum(expenses)/len(expenses))