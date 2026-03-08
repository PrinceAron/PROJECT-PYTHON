def check_clearance(func):
    def wrapper(*args,**kwargs):
        clearance_level = args[1]
        if clearance_level.upper() != "ADMIN":
            print("ACCESS DENIED: Low Clearance!") 
            return None
        else:
            print("ACCESS GRANTED: Welcome, Admin.")
        return func(*args,**kwargs)
    return wrapper  


@check_clearance
def get_server_data(user, level):
    return "Sensitive Data: 192.168.1.1"

# This should work
print(get_server_data("Prince", "ADMIN")) 

# This should fail
print(get_server_data("Guest", "STUDENT"))