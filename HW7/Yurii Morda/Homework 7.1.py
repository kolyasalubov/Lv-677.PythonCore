a = int(input("Input the first number =>"))
b = int(input("Input the second number =>"))

def max_param(first_param, second_param):
    """This funktion returning the biggest of 2 numbers"""
    if first_param > second_param:
        return first_param
    return second_param

print(max_param(a,b))    
