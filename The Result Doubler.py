## The Result Doubler

def double_result(func):
    def wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        result *= 2
        return result
    return wrapper

@double_result
def add(a, b):
    return a + b

@double_result
def square(n):
    return n * n

print(add(5, 5))   # Logic: (5+5) * 2 = 20
print(square(4))   # Logic: (4*4) * 2 = 32