input_number = int(input('Enter number "n" to print Fibonacci numbers:\n'))
first_number = 0
second_number = 1
count = 1
while count <= input_number: 
    print(first_number) 
    first_number,second_number = second_number, first_number+second_number
    count +=1
