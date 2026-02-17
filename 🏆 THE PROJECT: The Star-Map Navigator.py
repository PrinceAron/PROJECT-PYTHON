## 🏆 THE PROJECT: The Star-Map Navigator

def check_fuel_safety(galaxy_data, destination, current_fuel):
    if destination in galaxy_data:
        fuel_needed = galaxy_data[destination]["distance"] * 2
        if current_fuel >= fuel_needed:
            return {"status": "Safe", "remaining": current_fuel - fuel_needed}
        else:
            return {"status": "Danger", "needed": fuel_needed - current_fuel}
    else:
        return None
    
star_map = {
    "Alpha Centauri": {"distance": 4, "type": "Triple Star"},
    "Sirius": {"distance": 8, "type": "Binary Star"},
    "Vega": {"distance": 25, "type": "Main Sequence"}
}


target = input("Enter Targer Planet: ").capitalize()
while True: 
    try:
        print("--------------------------------")
        fuel_level = int(input("Enter Fuel Lebel: "))
        break
    except ValueError:
        print("--------------------------------")
        print("bugo gamit og Number oi")

mission_report = check_fuel_safety(star_map, target, current_fuel=fuel_level)

if mission_report is None:
    print(f"Error: {target.capitalize()} not in star-map.")
elif mission_report["status"] == "Safe":
    print(f"Jump successful! Fuel remaining: [{mission_report["remaining"]}].")
else:
    print(f"Insufficient fuel! You need {mission_report["needed"]} more units.")