## 1. The VIP Guest List

def check_guest(name_list, guest_name):
    if guest_name in name_list:
        return True
    else:
        return False

membership = ["prince","precious", "cyril", "ping", "lyka"]
while True:
    login = input("Please Enter Your Name: ").lower()
    if not login.isdigit():
        checking = check_guest(membership, guest_name=login)
        if checking:
            print(f"Hi {login.capitalize()} Enjoy Gym")
            break   
        else:
            print("No user have been found!!!")
            continue
    else:
        print("Please Enter Proper Name")
