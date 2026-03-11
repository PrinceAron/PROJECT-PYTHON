# # 🛡️ Level 1: Basic Input Protection
# try:
#     Age = int(input("Enter your age: "))
#     print(Age)
# except ValueError:
#     print("Bading KA")  

# # 🔄 Level 2: The Persistence Loop

# while True:
#     try:
#         Age = int(input("Enter your age: "))
#         print(f"You Are: {Age}")
#         break   
#     except ValueError:
#         print("Bading KA")

# Level 3: The Bulletproof Calculator

# while True:
#     try:
#         num1 = int(input("Enter Number 1: "))
#         num2 = int(input("Enter Number 2: "))
#         result = num1 / num2
#     except ValueError:
#         print("USE NUMBER BADING KA AH")
#     except ZeroDivisionError:
#         print("ZERO?? SUNTUKON TIKA RON WALAY ZERO")
#     else:
#         print(f"{num1} Divided by {num2} Equal to {result:.2f} ")
#         break 
#     finally:
#         print("System check complete.")

## 🚩 Project: The Custom Rule Enforcer


while True:
    try:
        age = int(input("Enter Your Age: "))
        if age < 18:
            raise ValueError("BATA PAKAY KA BOY!")
        if age > 100:
            raise ValueError("TANDA MONA MANONG AH VAMPIRA YARN?")
    except ValueError as e:
        print(e)
    else:
        print(f"You are {age} years old")
        print("WElCOME BOY")
        break 
