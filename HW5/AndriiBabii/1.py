div_by_2 = []
div_by_3 = []
other = []

for i in range(1,10):
    if i % 2 == 0:
        div_by_2.append(i)
    elif i % 3 == 0:
        div_by_3.append(i)
    else:
        other.append(i)

print(f"""
Even numbers that are divisible by 2: {div_by_2}
Odd numbers, which are divisible by 3: {div_by_3}
Numbers that are not divisible by 2 and 3: {other}
""")
