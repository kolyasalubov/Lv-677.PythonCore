# 6.1

def the_largest_number_of_two_numbers(first_number, second_number):
    '''
    The function returns the largest of two numbers
    entered by a user. If numbers are equal
    the function returns the first one
    '''
    if first_number == second_number:
        return first_number
    elif first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print(f"The largest of two numbers is {the_largest_number_of_two_numbers(first_number, second_number)}")
