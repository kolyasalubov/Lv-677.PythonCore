n = int(input("Введіть число n: "))
x = 1
fibo = [0, ]
while x <= n:
    fibo.append(x)
    x = x + fibo[-2]
    
for num in fibo:
    print(num, end = ", ")
    

