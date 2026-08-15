# Bonus Project — Inventory Manager
""""
Output
Warehouse Inventory
1. Carton A
2. Carton B
3. Carton C
4. Carton D
Total Products : 4"""

inventory = []
inventory.append("Carton A")
inventory.append("Carton B")
inventory.append("Carton C")
inventory.append("Carton D")

print("\n------ Warehouse Inventory ------\n")
for index , product in enumerate(inventory,start=1):
    print(f"{index}. {product}")
print("\nTotal Products: ",len(inventory))
