#Task3. Print Fibonacci numbers up to the entered number n, using cycles. 
#(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

enter_number = int(input("Enter your number: "))

fibonacci_1 = 1
fibonacci_2 = 0
for i in range(enter_number-1):
    fibonacci_1 += fibonacci_2
    fibonacci_2 = fibonacci_1 - fibonacci_2
    print(fibonacci_1, end=" ")
    