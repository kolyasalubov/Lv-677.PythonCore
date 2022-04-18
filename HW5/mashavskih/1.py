even = [x for x in range(10) if x%2 == 0]
odd = [x for x in range(10) if x%3 == 0]
not_divisible = [x for x in range(10) if x%3!= 0 and x%2!= 0]
print(f'Even number which are divisible by 2 - {even}')
print(f'Odd numbers which are divisible by 3 - {odd}')
print(f'Not divisible 3 and 2 - {not_divisible}')
