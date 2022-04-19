#number = input("Input your number => ")
#a = int(number[0])
#b = int(number[1])
#c = int(number[2])
#d = int(number[3])
#print("Сума цифр числа", a + b + c + d)




a = input("Input your number => ")
b = ''
for i in a:
    b = i + b
print(int(b))