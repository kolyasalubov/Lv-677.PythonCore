first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: ')) 

def largest_number():
    """The function that returns 
    the largest number of two numbers """

    if first_number > second_number:
        print(f'{first_number}  largest than {second_number}')
    elif first_number < second_number:
        print(f'{second_number} largest than {first_number}')
    else:
        print(f'{first_number} equal {second_number}')
largest_number()
