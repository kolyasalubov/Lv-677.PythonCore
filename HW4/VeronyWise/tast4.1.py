number = int(input('Write integer number for factorial:'))
factorial = 1
if number > 0:
    for i in range (1, number + 1):
        factorial = i * factorial
    print(f'{number}! = {factorial}')
else:
    print('Negative integer number or 0. Write a positiv number')
