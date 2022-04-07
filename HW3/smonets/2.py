number = 1992
number_str = str(number)
dobutok = int(number_str[0]) * int(number_str[1]) * int(number_str[2]) * int(number_str[3])
print(f"Добуток цифр цього числа = {dobutok}")

number_list_reversed_str = list(reversed(number_str))
number_reversed_str = number_list_reversed_str[0] + number_list_reversed_str[1] + number_list_reversed_str[2] + number_list_reversed_str[3]
print(f"Число в реверсивному порядку: {int(number_reversed_str)}")


number_sorted_list = sorted(number_str)
number_sorted_str = number_sorted_list[0] + number_sorted_list[1] + number_sorted_list[2] + number_sorted_list[3]
print(f"Посортовані цифри в даному числі: {int(number_sorted_str)}")


