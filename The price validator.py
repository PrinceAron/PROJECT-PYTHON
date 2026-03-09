def prevent_negative(func):
    def wrapper(*args,**kwargs):
        total = func(*args,**kwargs)
        if total < 0:
            total = 0
        return total
    return wrapper

@prevent_negative
def calculate_profit(income, expenses):
    return income - expenses

print(calculate_profit(100, 50)) 

print(calculate_profit(50, 100))