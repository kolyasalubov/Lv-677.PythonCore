# 1. Записати в стрічку філософію Пайтона 
# - Знайти в заданій стрічці кількість 
#   входжень слів (better, never, is)
# - Вивести весь текст у верхньому регістрі (всі великі літери)
# - Замінити всі входження символу “і” на “&”
# 2. Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число
# 3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

# 1. Записати в стрічку філософію Пайтона 
from numpy import sort


the_zen_of_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

print(the_zen_of_python)
# - Знайти в заданій стрічці кількість входжень слів (better, never, is)
print(the_zen_of_python.count('better'))
print(the_zen_of_python.count('never'))
print(the_zen_of_python.count('is'))
# - Вивести весь текст у верхньому регістрі (всі великі літери)
print(the_zen_of_python.upper())
print(the_zen_of_python.replace("i", "&"))
# 2. Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
number = input("Введите четырехзначное число :")
summ_number = int(number[0])+ int(number[1]) + int(number[2]) +  int(number[3])
print(summ_number)
# - Записати число в реверсному порядку.
print(number[::-1])
# - Посортувати цифри, що входять в дане число
sort_number_list= sorted(number)
sort_number_str= "".join(sort_number_list)
print(sort_number_str)
# 3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = "world"
b = str(12345)
# a = b
# b = a
a = a + b
b = a[:(len(b))]
a = a[(len(b)):]
print(a)
print(b)

