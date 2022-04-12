def zero_fuel(distance_to_pump, mpg, fuel_left):
    return 1 if distance_to_pump / fuel_left <= mpg else 0

# I noticed that I have extra code, so for better remember I added below the simplified version (idea was goten from codewars)
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / fuel_left <= mpg
