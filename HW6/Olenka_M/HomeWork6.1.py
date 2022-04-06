# What function of all this vertions we need to use depends on how and why we will use it
# I didn`t write type of input data and output data in DocString, becouse I wrote it in first line of every function
# print("\n-------------------------------------Version 0-----------------------------------\n")

def largest_number(number1: float,number2: float) -> float:
    """
    This function return the largest number of two numbers.
    If numbers are equals, function will return first of them.
    """    
    if number1 == number2:
        return number1
    elif number1 > number2:
        return number1
    else:
        return number2
        
# print("\n-------------------------------------Exemple of using -----------------------------------\n")

num1 = float(input("Please, enter first number: "))
num2 = float(input("Please, enter second number: "))

print(f"The largest of numbers is {largest_number(num1,num2)}")

# print("\n-------------------------------------Version 1-----------------------------------\n")

# def largest_number(number1: float,number2: float) -> float:
#     """
#     This function return the largest number of two numbers.
#     If numbers are equals, function will return None.#     
#     """    
#     if number1 == number2:
#         return None
#     elif number1 > number2:
#         return number1
#     else:
#         return number2

# print("\n-------------------------------------Exemple of using -----------------------------------\n")

# num1 = float(input("Please, enter first number: "))
# num2 = float(input("Please, enter second number: "))

# print(f"The largest of numbers is {largest_number(num1,num2)}" if {largest_number(num1,num2)} is None\
# else f"There is no the largest number. {num1} = {num2}")

# print("\n-------------------------------------Version 1-----------------------------------\n")

# def largest_number(number1: float,number2: float) -> str:
#     """
#     This function return informaition what number is the largest number of two numbers.
#     If numbers are equals, function will return informayion about it.
#     """
#     if number1 == number2:
#         return f'There is no the largest number. {number1} = {number2}'       
#     elif number1 > number2:
#         return f'The largest number is {number1}'       
#     else:
#         return f'The largest number is {number2}'

# print("\n-------------------------------------Exemple of using -----------------------------------\n")
    
# num1 = float(input("Please, enter first number: "))
# num2 = float(input("Please, enter second number: "))

# print(largest_number(num1,num2))
