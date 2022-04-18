num = int(input("Enter number from Fibonacci numbers: "))
First_val = 0
Second_val = 1
while Second_val <= num:
    print(Second_val)
    First_val,Second_val = Second_val, First_val + Second_val
print("done")