#print("Calculating factorial using while loop")

n = int(input("Input a number to calculate  factiorial : "))
fact = 1
while n > 0:
        fact = fact*n
        n = n - 1
print(f"Factorial equals: ", fact)

#print("calculating factorial using for loop")

n = int(input("Input a number to calculate  factiorial : "))
fact = 1
for b in range(1,n+1):
    fact = fact*b
print(f"Factorial equals: ", fact)