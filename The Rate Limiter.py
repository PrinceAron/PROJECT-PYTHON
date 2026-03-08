## The Rate Limiter

def limit_calls(func): 
    count = 0
    def wrapper(*args,**kwargs):
        nonlocal count
        count += 1
        if count > 3:
            print("BAWAL NA SUBRA NAKA")
            return None
        else:
            return func(*args,**kwargs)
    return wrapper


@limit_calls
def send_email(user):
    return f"Email sent to {user}"

print(send_email("Prince")) # Call 1: Success
print(send_email("Prince")) # Call 2: Success
print(send_email("Prince")) # Call 3: Success
print(send_email("Prince"))