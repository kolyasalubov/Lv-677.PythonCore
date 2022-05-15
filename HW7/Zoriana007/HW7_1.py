def square():
    
    figure = input("Please input number to calculate area (1 - rectangle, 2 - triangle, 3 - circle) :" )

    if figure == "1":
        a = float(input("Please input value a : "))
        b = float(input("Please input value b : "))
        rectangle = a*b
        return (f"Area of rectangle is {rectangle}")
         

    elif figure == "2":   
        a = float(input("Please input value a : "))
        h = float(input("Please input value h : "))
        triangle = 0.5*h*a
        return(f"Area of rectangle is {triangle}") 
        

    elif figure =="3":
        import math
        r = float(input("Please input value r : "))
        circle = math.pow((math.pi*r),2)
        return(f"Area of rectangle is {circle}") 
            
    else:
        return("Error, please choose figure from given numbers.")
        


print(square())

# Напишіть скрипт, який обчислює площу прямокутника a*b, площу
# трикутника 0.5*h*a, площу кола pi*r**2 і цей скрипт використати в іншому
# модулі, в якому ми запитуємо користувача площу якої фігури він хоче
# обчислити.

# (для виконання завдання необхідно імпортувати модуль math, а з нього
# функцію pow() та значення змінної пі, модуль1, який містить три функції для
# знаходження площ, модуль2, в якому імпортований модуль1 і виконується
# основна логіка програми).