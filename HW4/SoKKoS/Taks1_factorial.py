sum_factorial = 1
number_factorial = input('Enter an integer and a positive number ')
if number_factorial.isnumeric() and int(number_factorial) > 0:
    for i in range(2, int(number_factorial)+1):
        sum_factorial *= i
elif number_factorial == '0':
    sum_factorial = 1
else:
    sum_factorial = 'Number is not integer or positive'

print(sum_factorial)


