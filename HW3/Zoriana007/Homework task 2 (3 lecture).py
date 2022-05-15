number = input("Please input 4 digit number: ")

number_list = list(number) 

multiplication_number = int(number_list[0]) * int(number_list[1]) * int(number_list[2]) * int(number_list[3])

number_list_reversed = number_list.reverse()
number_reversed = "".join(number_list)


number_list_sorted = number_list
number_list_sorted.sort()
number_sorted = "".join(number_list_sorted)


print("Добуток цифр цього числа", multiplication_number,"\nЧисло в реверсному порядку", number_reversed,"\nПосортувати цифри, що входять в дане число: ", number_sorted)






# -Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число