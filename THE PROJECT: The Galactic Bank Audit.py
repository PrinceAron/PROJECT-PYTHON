## THE PROJECT: The Galactic Bank Audit
def audit_accounts(transaction_list, limit=100):
    flagged = []
    for transact in transaction_list:
        if transact["amount"] > limit or transact["amount"] <= 0:
            flagged.append(transact)
    return flagged

ledger = [
    {"id": "TX101", "name": "Alice", "amount": 500},
    {"id": "TX102", "name": "Bob", "amount": 2500},
    {"id": "TX103", "name": "Charlie", "amount": 800},
    {"id": "TX104", "name": "David", "amount": 1200}
]

while True:
    limitinput = input("Enter Amount: ")
    if limitinput.isdigit( ):
        limitinput = int(limitinput)
        break
    else:
        print("Please enter a valid amount.")


flagged_list = audit_accounts(transaction_list=ledger, limit=limitinput)

if not flagged_list:
    print("CLEAR")
else:
    for check in flagged_list:
        print(check["name"], check["amount"], check["id"])