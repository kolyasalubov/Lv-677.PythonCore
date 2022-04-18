nums = int(input("input number: "))

factorial = 1
for i in range(nums+1):
    if i != 0:
        factorial *= i
    print(factorial)
