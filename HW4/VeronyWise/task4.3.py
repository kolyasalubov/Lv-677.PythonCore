number_for_fibonacci = int(input("Enter Fibonacci number: "))
first_num = 0
second_num = 1
while second_num <= number_for_fibonacci:
    print(second_num)
    first_num, second_num = second_num, first_num + second_num
print("Fibonacci number")