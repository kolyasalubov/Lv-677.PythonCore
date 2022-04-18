#4.1
input_number = int(input("Enter a natural number: "))
factorial = 1
for i in range(1, input_number+1):
    factorial = factorial * i
print(factorial)