# Lv-677_Ivan_Vaulin

# Task1. In the range from 1 to 10 determine 
# Even numbers that are divisible by 2,
# Odd numbers, which are divisible by 3,
# Numbers that are not divisible by 2 and 3.

x = []
for b in range(1, 11):
    if b % 2 == 0:
        print(f'Even numbers that are divisible by 2 - {b}')
    elif b % 2 != 0:
        if b % 3 == 0:
            print(f'Odd number, witch ar divisible by 3 - {b}')
        elif b % 2 != 0:
            if b % 3 != 0:
                print(f'Numbers that are not divisible by 2 and 3 - {b}')