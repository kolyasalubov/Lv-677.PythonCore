import scrypt_module

radius = input("Площу чого ти хочеш обчислити ? (rectangle/triangle/circle) ")
if radius == "rectangle":
    a = int(input("Вкажи сторону 1: "))
    b = int(input("Вкажи сторону 2: "))
    print(f"Площою такого прямокутника є {scrypt_module.area_rectangle(a,b)}")
elif radius == "triangle":
    a = int(input("Вкажи найбільшу сторону трикутника: "))
    h = int(input("Вкажи висоту трикутника: "))
    print(f"Площою такого трикутника є {scrypt_module.area_triangle(a,h)}")
elif radius == "circle":
    r = int(input("Вкажи радіус круга: "))
    print(f"Площою такого круга буде {scrypt_module.area_circle(r)}")
else:
    print("Неправильний вибір!!!")
    