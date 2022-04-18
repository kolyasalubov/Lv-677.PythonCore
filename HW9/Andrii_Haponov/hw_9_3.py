# 81
# Create an Create an employee class. Each employee has characteristics such 
# as name and salary. The class should have a counter that calculates the total number of employees, 
# as well as a method that prints the total number of employees and a method that displays information 
# about each employee in particular, namely the name and salary.

# In addition to creating a class, display information about the base classes 
# from which the employee class is inherited (__base__), the class namespace (__dict__), 
# the class name (__name__), the module name 
# in which the class is defined (__module__), the documentation bar ( __doc__) 

# Создайте класс «Создать сотрудника». У каждого сотрудника есть такие характеристики, как имя и зарплата. 
# В классе должен быть счетчик, подсчитывающий общее количество сотрудников, 
# а также метод, выводящий общее количество сотрудников и метод, выводящий информацию 
# о каждом сотруднике в частности, а именно ФИО и оклад.

# Помимо создания класса отображать информацию о базовых классах, от которых наследуется 
# класс сотрудника (__base__), пространстве имен класса (__dict__), имени класса (__name__), 
# имени модуля, в котором класс определен (__module__) , панель документации ( __doc__)

class Create_an_employee():
    """Create an Create an employee class"""
    counter = 0
    inf = {}
    def __init__(self, name, salary):
        Create_an_employee.counter += 1
        new_emloeer = {name: salary}
        Create_an_employee.inf.update(new_emloeer)
        self.__name = name
        self.__salary = salary

    def Total_employees(counter):
        return f"There are employees: {Create_an_employee.counter}"

    def Information_about_each_employee(self):
        return   f"There are emploee : {Create_an_employee.inf}"
        
    def __del__(self):
        Create_an_employee.counter -= 1



emploer_1 = Create_an_employee("Anton", 8000)
emploer_2 = Create_an_employee("Lora", 6000)

# inf ={}
# a = {"Anton": 8000}
# b = {"Lora": 6000}
# x = {**a, **b}
# x = b.update(a)

print(emploer_1.Total_employees())
print(emploer_1.Information_about_each_employee())

    
