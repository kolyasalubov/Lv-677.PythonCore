# Task2. Create a list that contains elements of integer type,
#  then use the loop to change the type of these elements to a floating type. 

# Создать список который содержит элементы целочисленного типа,
# затем используйте цикл, чтобы изменить тип
# этих элементов к плавающему типу.

list_int_type = []
while True:
    int_type = int(input("Enter number > 0, if 0 break list : ")) 
    if int_type == 0:
        break
    else:
        list_int_type.append(int_type)
print(list_int_type)

list_float_type = []
for i in list_int_type:
    float_type = float(i)
    list_float_type.append(float_type)
print(list_float_type)




