user_profile = {"name": "Prince", "clearance": 5}

def clearance_check(required_level):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if user_profile["clearance"] >= required_level:
                result = func(*args,**kwargs)
                return result
            else:
                print("ERRORR")
        return wrapper
    return decorator
    

@clearance_check(1)
def enter_lobby():
    print("You Are In the Lobby Level")

@clearance_check(5)
def enter_office():
    print("You Are In the Office Level")

@clearance_check(10)
def enter_vault():
    print("You Are In the Vault Level")

enter_lobby()
enter_office()
enter_vault()