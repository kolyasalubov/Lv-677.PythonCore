n_number_fibo = int(input("Print Fibonacci numbers up to the entered number n (Integer and more 0): "))
first_num = 1
second_num = 1
if n_number_fibo > 0:
    while second_num < n_number_fibo:
       sum_first_second = first_num  + second_num
       first_num , second_num = second_num, sum_first_second
       print(first_num)
else:
    print("Number less than 1")