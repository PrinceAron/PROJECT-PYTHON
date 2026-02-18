## 🏁 The Final Decorator Challenge: The Execution Timer

call_count = 0

def track_calls(func):
    def wrapper(*args,**kwargs):
        global call_count
        call_count += 1
        print(f"Execution #{call_count} starting...")

        result = func(*args, **kwargs)
        return result
    return wrapper

@track_calls
def multiply(a,b):
    return a * b


print(f"Result: {multiply(10, 2)}")
print(f"Result: {multiply(5, 5)}")