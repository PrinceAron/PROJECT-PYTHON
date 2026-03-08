## "The Multi-Tool"

def debug_info(func):
    def wrapper(*args,**kwargs):
        print(f"Arguements Received: {args}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@debug_info
def add_numbers(a, b):
    return a + b

@debug_info
def identify_student(name, course):
    return f"Student: {name} | Course: {course}"

# Run them both
print(add_numbers(10, 25))
print(identify_student("Prince", "BSIT"))