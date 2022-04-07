even_div2 = []
odd_div3 = []
not_div2_3 = []
for i in range(1,11):
    if i % 2 == 0:
        even_div2.append(i)
    elif i % 2 != 0 and i % 3 == 0:
        odd_div3.append(i)
    elif i % 2 != 0 and i % 3 != 0: 
        not_div2_3.append(i)
        
print(f"""Парні числа, які діляться на 2: {even_div2}
Непарні числа, які діляться на 3: {odd_div3}
Числа які не діляться на 2 і на 3: {not_div2_3}""")