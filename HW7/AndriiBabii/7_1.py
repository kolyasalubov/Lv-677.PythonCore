# Напишіть скрипт, який обчислює площу прямокутника a*b, 
# площу трикутника 0.5*h*a, площу кола pi*r**2 
# і цей скрипт використати в іншому модулі, 
# в якому ми запитуємо користувача площу якої фігури він хоче обчислити. 

# (для виконання завдання необхідно імпортувати  модуль math, 
# а з нього функцію pow() та значення змінної пі, модуль1, 
# який містить три функції для знаходження площ, модуль2, 
# в якому імпортований модуль1 і виконується основна логіка програми).

import module1

def shape_picker(a):
    if a == 1:
        return module1.area_circle(float(input("Input radius of circle: ")))
    elif a == 2:
        return module1.area_triangle(
            float(input("Input side: ")), 
            float(input("Input height: ")))
    elif a == 3:
        return module1.area_rectangle(
            float(input("Input first side: ")), 
            float(input("Input second side: ")))
    else:
        return None

print(shape_picker(int(input(
"""
Введіть:
1 - Для обчислення площі кола
2 - Для обчислення площі трикунтника
3 - Для обчислення площі прямокутника
"""))))
