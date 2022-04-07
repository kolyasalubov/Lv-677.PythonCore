input_number = int(input('Enter your Fibonacci number : '))
first_number = 0
second_number = 1
fibonacci_numbers = []

while first_number <= input_number:
    fibonacci_numbers.append(first_number) 
    first_number,second_number = second_number, first_number+second_number
print (fibonacci_numbers)