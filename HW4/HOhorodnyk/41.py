number_to_factorial = int(input("Enter a number:"))

factorial = 1 

if number_to_factorial < 0:
    print("The factorial isn't exist")

elif number_to_factorial == 0:
    print("The factorial of 0 is 1")
    
else:
    for i in range(1,number_to_factorial + 1):
        factorial = factorial*i
    print ("The factorial of",number_to_factorial,"is",factorial)