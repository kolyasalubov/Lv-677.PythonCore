fibonacci_number = int(input("Enter you number: "))
fibonacci_number_1 = [0, 1]
for i in range(2, fibonacci_number):
    fibonacci_sum = fibonacci_number_1[i-1] + fibonacci_number_1[i-2]
    fibonacci_number_1.append(fibonacci_sum)
print(fibonacci_number_1)
