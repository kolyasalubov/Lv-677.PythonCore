number = input("Input 4 digit number: ") #Получам 4-х значне число

number_list = list(number) #Переводим число в список

#Перемножаємо кожний елемент списка
product_number = int(number_list[0]) * int(number_list[1]) * int(number_list[2]) * int(number_list[3])


#Реверсування та поєднання списку
number_list_reversed = number_list.reverse()
number_reversed = "".join(number_list)

#Сортировка та поєднання списку
number_list_sorted = number_list
number_list_sorted.sort()
number_sorted = "".join(number_list_sorted)

#Вивід
print("\nProduct: ", product_number,"\nReversed: ", number_reversed,"\nSorted: ", number_sorted)
