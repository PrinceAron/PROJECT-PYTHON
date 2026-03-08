def shout_decorator(func):
    def wrapper(name):
        result = func(name).upper() + "!"
        return result
    return wrapper

@shout_decorator
def greet(name):
    return F"Hello, {name}"

print(greet("Prince"))