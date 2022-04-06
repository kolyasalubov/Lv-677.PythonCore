num_div_2 = []
num_div_3 = []
num_div_not2_3 = []

for number in range(1,11):
    if number %2 == 0:
        num_div_2.append(number)    
    elif number %3 == 0:
        num_div_3.append(number)
    else:
        num_div_not2_3.append(number)
        
print(f'num_div_2: {num_div_2} \nnum_div_3: {num_div_3} \nnum_div_not2_3: {num_div_not2_3}')