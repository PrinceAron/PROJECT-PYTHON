## 2. The Temperature Converter

def converter(Celsius, Fahrenheit, operator="Celsius"):
    if operator.capitalize() == "Celsius":
        return (9/5 * Celsius) + 25 
    else:
        return (Fahrenheit - 32) / 1.8

while True:
    try:
        cel = int(input("Enter Celsius: "))
        fah = int(input("Enter Fahrenheit: "))
        op =  input("you will convert it into?: ")
        break
    except ValueError:
        print("ERRORR")