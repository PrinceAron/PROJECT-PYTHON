##  Mini-Project: The Secure Vault System

current_user = {"username": "Prince", "is_logged_in": True}

def log_transaction(func):
    def wrapper(*args,**kwargs):
        print("Starting transaction...")
        result = func(*args,**kwargs)
        print("Transaction complete.")
        return result
    return wrapper

def require_auth(func):
    def wrapper(*args,**kwargs):
        if current_user["is_logged_in"]:
            result =func(*args,**kwargs)
            return result
        else:
            print("ACCESS DENIED: Please log in.")
    return wrapper

@log_transaction
@ require_auth
def view_balance():
    print("Your balance is $5,000.")

@require_auth
def withdraw_money(amount):
    print(f"Withdrawing ${amount}...")

view_balance()

withdraw_money(100)