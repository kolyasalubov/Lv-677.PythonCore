# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).
def num(x3, x4):
    """ 
    This function shows the largest number of two numbers

    """
    if x3 > x4: 
        return x3
    elif x3 == x4:

        return x3
    elif x4 > x3:
        return x4
x1 = int(input("number 1: "))
x2 = int(input("number 2: "))
print (f"largest number of two numbers", num(x1,x2))