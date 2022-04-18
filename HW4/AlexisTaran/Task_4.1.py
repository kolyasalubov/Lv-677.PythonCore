number = int(input("Enter the number for which factorial value to be determined: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(f"The factorial number {number} is: {factorial}")
