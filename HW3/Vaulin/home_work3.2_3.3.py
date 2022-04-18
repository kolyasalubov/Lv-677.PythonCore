# Lv-677.PythonCore
# -Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

x = int(input('Напишiть чотирицифрове натуральне число: '))
while len(str(x)) != 4:
    print("Error")
    x = int(input("Напишiть чотирицифрове натуральне число: "))
else:
    print(f'Ваше число - {x}')
    num_l = []
    for num in str(x):
        num_l.append(num)
print(f"Добуток числа {x} = ",
    int(num_l[0]) * int(num_l[1]) * int(num_l[2]) * int(num_l[3]))

print("Число в реверсному порядку ")
list_reverse = (num_l[::-1])
print(''.join(list_reverse))

print(sorted(num_l))

#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = ("1")
b = ("2")
print(b.replace('2','1'), a.replace('1', '2'))

a, b = 2, 3
a, b = b, a
print (a)