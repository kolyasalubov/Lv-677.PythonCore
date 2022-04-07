def area_rectangle(a, b):
    """ 
    calculates the area of a rectangle
    where:
    a = side1
    b = side2
    """
    
    return a * b

def area_triangle(a, h):
    """ 
    calculates the area of a triangle
    where: 
    a = base of triangle
    h = height of triangle
    """
    
    return 0.5 * a * h

def area_circle(r):
    """ 
    calculates the area of circle
    where:
    r = radius of circle
    """
    
    return  3.14159 * (r**2)

radius = input("Площу чого ти хочеш обчислити ? (rectangle/triangle/circle) ")
if radius == "rectangle":
    a = int(input("Вкажи сторону 1: "))
    b = int(input("Вкажи сторону 2: "))
    print(f"Площою такого прямокутника є {area_rectangle(a,b)}")
elif radius == "triangle":
    a = int(input("Вкажи найбільшу сторону трикутника: "))
    h = int(input("Вкажи висоту трикутника: "))
    print(f"Площою такого трикутника є {area_triangle(a,h)}")
elif radius == "circle":
    r = int(input("Вкажи радіус круга: "))
    print(f"Площою такого круга буде {area_circle(r)}")
else:
    print("Неправильний вибір!!!")