num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

def return_max_number(number_1, number_2):
    '''
    This func returns max number from two entered number
    '''
    number_1 = float(number_1)
    number_2 = float(number_2)

    if number_1 == number_2:
        return f'{number_1} is equal to {number_2}'
    if number_1 > number_2:
        return f'max number is {number_1}, min number is {number_2}'
    else:
        return f'max number is {number_2}, min number is {number_1}'

print(return_max_number(num1, num2))
