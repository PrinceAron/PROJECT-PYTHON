# 1. We define the user's role outside the functions
user_role = "admin" 

# 2. The Decorator (The Security Guard's Training)
def requires_admin(func):
    # The Wrapper (The Guard standing at the door)
    def wrapper():
        # The Check: Is the role correct?
        if user_role == "admin":
            print("Access Granted.")
            func()  # The Guard opens the door and lets the function run
        else:
            print("Access Denied: Admin privileges required.")
            
    # The Return (Handing the Guard over to the program)
    return wrapper

# 3. Applying the Decorator
@requires_admin
def delete_database():
    print("Database deleted successfully!")

# 4. Running the function
delete_database()