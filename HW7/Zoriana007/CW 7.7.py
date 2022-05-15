def counting_sheeps (array_of_ships: list):
    sum = 0
    for sheep in array_of_ships:
        if sheep == True:
            sum += sheep
    return sum
        
        
print("Sum of sheeps is : ", counting_sheeps([True, True, True, False, False, True]))
print("Sum of sheeps is : ", counting_sheeps([True, True, True, False, False, True, True]))
print("Sum of sheeps is : ", counting_sheeps([True, True, True, False, True, True, True]))





# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined