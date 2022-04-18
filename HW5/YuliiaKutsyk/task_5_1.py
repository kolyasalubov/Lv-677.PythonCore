list_even = [n for n in range(1,10) if n % 2 == 0]
list_odd = [n for n in range(1,10) if n % 3 == 0]
list_not_divided = [n for n in range(1,10) if n % 2 != 0 and n % 3 != 0]
print(f'Even numbers: {list_even}\n')
print(f'Odd numbers: {list_odd}\n')
print(f'Numbers that are not divisible by 2 and 3: {list_not_divided}\n')
