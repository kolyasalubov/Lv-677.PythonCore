#4.3
user_integer = int(input("Enter a positive integer: "))
a = 0
b = 1
while b <= user_integer:
    print(b)
    a, b = b, a + b
print("The end")
