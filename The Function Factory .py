##The Function Factory 

def power_builder(p):
    return lambda x: x ** p

square = power_builder(2)
cube = power_builder(3)

print(square(5),cube(5))