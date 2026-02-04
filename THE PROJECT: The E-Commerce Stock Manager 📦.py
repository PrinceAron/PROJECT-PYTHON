# THE PROJECT: The E-Commerce Stock Manager 📦

inventory = {"phone": 10, "laptop": 5, "tablet": 8}

price_list = {"phone": 500, "laptop": 1200, "tablet": 300}

sales_history = []

while True:
    opnum = ["1","2","3","4"]
    option = ["[1] VIEW STOCK",

        "[2] BUY ITEM",

        "[3] RESTOCK",

        "[4] EXIT"]
    
    print(f"Please Select in this: {option}")
    select = input(f"ENTER:")

    if select.isdigit() and select in opnum:
        if select == "1":
            
    else:
        print("Please Enter Degit on option only")
        print(f"Please Select in this: {option}")
        continue