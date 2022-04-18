# Task3. Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

# Печать чисел Фибоначчи до введенного числа n, с помощью циклов.
# (Последовательность чисел Фибоначчи
#   0, 1, 1, 2, 3, 5, 8, 13 и т.д.)




number_fibonacci = int(input("Enter number : "))
f1 = 0
f2 = 1

while number_fibonacci > 2:
    f1, f2 = f2, f1 + f2
    print(f1, end=' ')
    number_fibonacci -= 1 

for i in range(2, number_fibonacci):
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")


