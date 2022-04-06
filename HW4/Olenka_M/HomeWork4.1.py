entered_number = int(input("Enter not negative integer number for getting factorial of the number: "))

if entered_number == 0:
   print(f"{entered_number}! = 1")
elif entered_number < 0:
    print(f"{entered_number} < 0, please, enter positive integer number or 0")
else:
    factorial_of_number = 1
    for i in range(1,entered_number+1):
            factorial_of_number = factorial_of_number * i
    print(f"{entered_number}! = {factorial_of_number}")
