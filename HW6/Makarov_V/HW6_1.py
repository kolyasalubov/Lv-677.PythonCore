def largest(a, b):
    """
    This function takes two numbers
    to determine which one is larger
    """
    if a > b:
        larger = a
    else:
        larger = b
    return larger


a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
larger = largest(a, b)
print(f"The largest number among a =  {a} and b = {b} is {larger}")
