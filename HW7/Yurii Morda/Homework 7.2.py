print("1- прамокутник , 2 - трикутник, 3 - коло")
n = int(input("Введіть номер фігури площу якої ви хочете обчислити"))
if n == 1:
    a = int(input("Введіть довжину прямокутника "))
    b = int(input("Введіть ширину прямокутника"))
    s = a*b
    print(f"Площа прямокутника:{s}")
if n == 2:
    print("Введіть сторони трикутника")
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    from math import sqrt
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площа трикутника: {s}")
if n == 3:  
    r = int(input("Радіус кола"))
    from math import pi
    s = (pi * r ** 2)
    print(f"Площа круга: {s}")

