## 🏆 THE PROJECT: The Cyberpunk Vending Machine.py

inventory = {
    "Cyber-Cola": {"price": 5, "stock": 10},
    "Synth-Snack": {"price": 3, "stock": 2},
    "Neon-Noodle": {"price": 12, "stock": 5}
}

def process_purchase(items_dict, requested_item, quantity):
    if requested_item in items_dict:
        if quantity <= items_dict[requested_item]["stock"]:
            total = items_dict[requested_item]["price"] * quantity
            items_dict[requested_item]["stock"] -= quantity
            return {"status": "Success", "total_cost": total}
        else:
            return {"status": "Low Stock", "available": items_dict[requested_item]["stock"]}
    else:
        return None
    
wants = input("What Do you want?: ").title().replace(" ", "-")
while True:
    try:
        pila = int(input("How much??: "))
        if pila <= 0:
            print("Bawal Negative")
            continue
        break
    except ValueError:
        print("Bawal letter number ra ba")

receipt = process_purchase(inventory, quantity=pila,requested_item=wants)

if receipt is None:
    print("Wami ana man!!!")
elif receipt["status"] == "Success":
    print(f"Purchase complete! Total: ${receipt['total_cost']}. Remaining stock: {inventory[wants]['stock']}.")
elif receipt["status"] == "Low Stock":
    print(f"Sorry, we only have {inventory[wants]['stock']} left.")
