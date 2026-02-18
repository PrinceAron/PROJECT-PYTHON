## 🎯 Task: The "Double-Space" Decorator

def make_space(func):
    def wrapper(*args,**kwargs):
        print("")
        result = func(*args,**kwargs)
        print("")
        return result
    return wrapper

@make_space
def say_hi(name):
    return f"Hi {name}!"

print(say_hi("butiti"))