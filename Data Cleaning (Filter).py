## Data Cleaning (Filter)

numbers = [12, 25, 30, 44, 55, 60, 72]
divisibleByfive = list(filter(lambda x: x % 5 == 0, numbers))
print(divisibleByfive)