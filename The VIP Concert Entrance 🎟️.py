fans_to_process = []

vip_list = []

general_list = []

for i in range(3):
    ticket = {}
    ticket["name"] = input("Enter your Name: ")
    ticket["age"] = int(input("Enter your age: "))
    ticket["Ticket_Code"] = input("Enter Ticket Code: ")
    fans_to_process.append(ticket)

for Check in fans_to_process: # Error 1: You are looping through 'ticket' (the last person only)
    if Check["Ticket_Code"].startswith("VIP") and Check["age"] >= 18:  # Error 2: You used "code" but named it "Ticket_Code" above
        Check["status"] = "VIP ACCESS" #ERROR 3: CHANGE TICKET TO CHECK
        vip_list.append(Check) # ERROR 4: append to vip_list not fans_to_process
    else:
        Check["status"] = "GENERAL"
        general_list.append(Check) # ERROR 5: append to general_list not fans_to_process

# Phase 3: Output I didnt learn this yet
print("\n--- VIP LIST ---") 
for v in vip_list:
    print(v)

print("\n--- GENERAL LIST ---")
for g in general_list:
    print(g)

