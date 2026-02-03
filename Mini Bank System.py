account = {"1001": 5000, "1002" : 3000 }
accountlog = input("Enter Account Number: ")
opperationList = ["DEPOSIT", "WITHDRAW", "CHECKBALANCE"]
logTry = 3

while True:
    if accountlog in account.keys():
        print(f"Hi user {accountlog} Welcome to our Mini Bank System")
        print("-----------------------------------------------------")
        print("Please select this option", opperationList)
        opperation = input("What do you want to do: ")
        breakpoint

        if opperation.lower() == "deposit":
            print(f"-----------------------{opperation}-----type back to go back------------")
            deposit = input("How much money do you want to deposit : ")
            if deposit.isdigit():
                depositf = int(deposit)
                if depositf > account[accountlog] or depositf <= 0:
                    print("You can't deposit beyond to your limit")
                else:
                    account[accountlog] += depositf
                    print(f"-----------------------{opperation}-----type back to go back------------")
                    print(f"You deposit: {depositf}")
            elif deposit.lower() == "back":
                print("-----------------------------------------------------")
                print(f"Hi user {accountlog} Welcome to our Mini Bank System")
                print("Please select this option", opperationList)
                opperation = input("What do you want to do: ")


    else:
        print("-----------------------------------------------------")
        print(f"{accountlog} NOT FOUND!!!")
        print(f"Please try Again {logTry}:")
        accountlog = input(f"Enter Account Number: ")
        logTry -= 1
        if logTry <= 0:
            print("-----------------------------------------------------")
            print("Please Try Again Later")
            break
