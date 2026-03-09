##  Unit Conversion (Map)

celsius_temps = [0, 20, 30, 100]
converter = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(converter)