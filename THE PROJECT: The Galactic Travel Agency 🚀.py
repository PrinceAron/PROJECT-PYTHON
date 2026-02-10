## THE PROJECT: The Galactic Travel Agency 🚀

def calculate_trip(destination, passengers, travel_class="economy", insurance=True):
    # 1. Start with the base price for ONE person
    price_per_person = 1000 
    
    # 2. Add the extra cost IF they are business class
    if travel_class.lower() == "business":
        price_per_person += 500 

    # 3. Calculate total for ALL passengers
    total = price_per_person * passengers

    # 4. Add the flat insurance fee at the very end
    if insurance:
        total += 200
    print(f"Trip to {destination} for {passengers} in {travel_class.capitalize()} costs ${total}.")

calculate_trip("Mars",2)
print()
calculate_trip("Jupiter",5,insurance=False,travel_class="Business")
print()
calculate_trip("Saturn",1)

