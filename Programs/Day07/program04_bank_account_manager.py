# Program 4 — Bank Account Manager
account = {"Account No": "PK001", "Name": "Annus", "Balance": 50000}

print("------ Bank Account ------")
for key, value in account.items():
    print(f"{key:<12} :{value}")
deposit = int(input("\nEnter Deposit Amount :"))
account["Balance"] += deposit
print("\nUpdated Balance :", account["Balance"])


# Challenge: Add a withdrawal feature with a balance check.
def withdrawal(amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount <= account["Balance"]:
        account["Balance"] -= amount
        print("Withdrawal Successful!")
        print(f"Remaining Balance :{account['Balance']}")
    else:
        print("Insufficient Balance!")
        print("Available Balance :", account["Balance"])


enter = int(input("\nEnter Withdrawal Amount :"))
withdrawal(enter)