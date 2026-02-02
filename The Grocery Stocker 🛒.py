# The Grocery Stocker 🛒 
# 70

in_stock = ["apple", "milk", "bread", "eggs"]
delivery_truck = []

for i in range(2):
    print(f"\n--- Box {i+1} ---")
    box = {}
    box["id"] = input("Please Enter Box ID: ").upper()
    
    box["contents"] = []
    
    for x in range(3):
        contents = input(f"Please enter item {x+1}: ").lower().strip() # I use split not strip I create another list
        box["contents"].append(contents)
    
    delivery_truck.append(box)

for validation in delivery_truck:
    all_present = True
    
    for Items in validation["contents"]: #MISTAKE validation i PUT box
        if Items not in in_stock: 
            all_present = False
            break
    
    if all_present: # I create new dict as validation
        validation["status"] = "SHELF"  
    else:
        validation["status"] = "BACKROOMS"

print("\n" + "="*30)
print("FINAL REPORT:")
for check in delivery_truck:
    print(check)