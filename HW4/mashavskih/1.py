number_to_find_factorial = int(input('Wright number:\n'))
factorial_of_number = 1
for objective_of_programme in range(2, number_to_find_factorial + 1):
    factorial_of_number *= objective_of_programme
print(f'{factorial_of_number}')
