## THE PROJECT: The VIP Security & Ticketing System

# SEMESTER 2: The Function (Logic)
def process_ticket(age, code, base_price=500):
    # .startswith() is safer for codes like VIP101
    if code.upper().startswith("VIP") and age >= 18:
        status = "VIP ACCESS"
        final_price = base_price + 1000
    else:
        status = "GENERAL"
        final_price = base_price
        
    return {"status": status, "price": final_price}

# SEMESTER 1: The Database & Loop
master_database = []

for i in range(3):
    print(f"\n--- Entry {i+1} ---")
    fan = {}
    fan["name"] = input("Name: ")
    fan["age"] = int(input("Age: "))
    fan["code"] = input("Code: ")
    
    # INTEGRATION: Call the function and save the dictionary result
    result = process_ticket(age=fan["age"], code=fan["code"])
    
    # Combine the function result into our fan dictionary
    fan.update(result) 
    
    # Save the complete fan to our database
    master_database.append(fan)

# --- FINAL OUTPUT ---
print("\n--- FINAL MASTER DATABASE ---")
for person in master_database:
    print(person)