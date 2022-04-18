import module1

select_area = input("""площу якої фігури хочете обчислити?\n
1. Прямокутник   
2. Трикутник
3. Коло\n
""")

if select_area == "1":
    a = float(input("Обчислюємо площу прямокутника a*b\nВведіть зміну a = "))
    b = float(input("Введіть зміну b = "))
    print(f"Площа прямокутника = {module1.area_rectangle(a, b)}")
elif select_area == "2":
    h = float(input("Обчислюємо площу трикутника 0.5*h*a\nВведіть зміну h = "))
    a = float(input("Введіть зміну b = "))
    print(f"Площа трикутника = {module1.area_triangle(h, a)}")
elif select_area =="3":
    r = float(input("Обчислюємо площу кола pi*r**2\nВведіть зміну r = "))
    print(f"Площа кола = {module1.area_circle(r)}")