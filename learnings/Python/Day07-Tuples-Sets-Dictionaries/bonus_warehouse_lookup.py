# Bonus Project — Warehouse Product Lookup
warehouse = {
    "P001": "Carton A",
    "P002": "Carton B",
    "P003": "Carton C",
    "P004": "Carton D"
}

print("------ Warehouse Products ------")
for code,product in warehouse.items():
    print(f"{code} -> {product}")

search = input("\nEnter Product Code: ").upper()
if search in warehouse:
    print("Product:", warehouse[search])
else:
    print("Product Not Found")
