account = {"1001": 5000, "1002" : 3000 }
accountlog = input("Enter Account Number: ")
opperationList = ["DEPOSIT", "WITHDRAW", "CHECKBALANCE", "EXIT"]
logTry = 3

while True:
    if accountlog in account:
        print(f"\nHi user {accountlog} | Welcome to our Mini Bank System")
        print("-----------------------------------------------------")
        print(f"Options: {opperationList}")
        operation = input("What do you want to do: ").upper().strip()

        # 1. EXIT LOGIC
        if operation == "EXIT":
            print("Thank you for using Mini Bank. Goodbye!")
            break

        # 2. CHECK BALANCE LOGIC
        elif operation == "CHECKBALANCE":
            print(f"\n[BALANCE] Your current balance is: ${account[accountlog]}")

        # 3. DEPOSIT LOGIC
        elif operation == "DEPOSIT":
            print(f"\n--- {operation} --- (Type 'back' to return)")
            amount = input("How much money do you want to deposit: ").lower().strip()
            
            if amount == "back":
                continue # Jumps back to the top of the while loop
            
            if amount.isdigit():
                amount_int = int(amount)
                if amount_int > 0:
                    account[accountlog] += amount_int
                    print(f"Success! You deposited ${amount_int}. New balance: ${account[accountlog]}")
                else:
                    print("Error: Deposit must be greater than 0.")
            else:
                print("Error: Please enter a valid number.")

        # 4. WITHDRAW LOGIC
        elif operation == "WITHDRAW":
            print(f"\n--- {operation} --- (Type 'back' to return)")
            amount = input("How much money do you want to withdraw: ").lower().strip()
            
            if amount == "back":
                continue
            
            if amount.isdigit():
                amount_int = int(amount)
                # CHECK LIMIT: Cannot withdraw more than you have
                if amount_int > account[accountlog]:
                    print(f"Transaction Declined: Insufficient funds. (Max: ${account[accountlog]})")
                elif amount_int <= 0:
                    print("Error: Withdrawal must be greater than 0.")
                else:
                    account[accountlog] -= amount_int
                    print(f"Success! You withdrew ${amount_int}. Remaining balance: ${account[accountlog]}")
            else:
                print("Error: Please enter a valid number.")
        
        else:
            print("Invalid Option. Please choose from the list.")

    # LOGIN FAILURE LOGIC
    else:
        logTry -= 1
        if logTry <= 0:
            print("-----------------------------------------------------")
            print("Too many failed attempts. Access Locked.")
            break
        print("-----------------------------------------------------")
        print(f"ACCOUNT {accountlog} NOT FOUND!!!")
        accountlog = input(f"Please try again. Enter Account Number ({logTry} tries left): ")