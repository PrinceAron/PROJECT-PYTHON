## The Activity Logger

def log_activity(func):
    def wrapper():
        print("Starting The Process...")
        func()
        print("Process completed successfully.")
    return wrapper

@log_activity
def fetch_data():
    print("Loading data from server...")

fetch_data()