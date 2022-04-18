# Lv-677.PythonCore

## Home Work 3.2

fibo = int(input("Enter your number :"))
num_1 = 0
num_2 = 1
count = 1
while count <= fibo:
    print (num_1)
    num_1, num_2 = num_2, num_1+num_2
    count +=1
