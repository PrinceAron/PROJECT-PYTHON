mylist = []

for i in range(3):
    mydict = {}
    mydict["firstname"] = input("Enter Your first name: ")
    mydict["lastname"] = input("Enter Your last name: ")
    mydict["age"] = input("Enter Your age: ")
    mydict["address"] = input("Enter Your address: ")
    mylist.append(mydict)

for check in mylist:
    print(check["firstname"], check["lastname"])