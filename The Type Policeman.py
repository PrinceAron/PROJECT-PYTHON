## The Type Policeman

def require_int(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) != int:
                print("Error: All arguments must be integers!")
                return None
        return func(*args, **kwargs)
    return wrapper

@require_int
def add_coords(x, y):
    return x + y

print(add_coords(10, 20))      # Should work: 30
print(add_coords(10, "20"))    # Should fail: Error message and None