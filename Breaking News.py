def make_announcement(func):
    def wrapper(*args,**kwargs):
        original_result = func(*args,**kwargs)
        fromatted_string = f">>> {original_result} <<<"
        return fromatted_string
    return wrapper

@make_announcement
def get_status():
    return "All Systems GO"

print(get_status())