class Employee():

    count = 0
    def __init__(self, name, salary ):
        self.name = name
        self.salary = salary
        Employee.count +=1
    def dispEmployee(self):
        return print(f'There are {Employee.count} employee in dpt.')

    def dispInfo(self):
        return print(f'Name: {self.name}\nSalary: {self.salary}')

a =Employee('Stepan', 30000)
b =Employee('Mykola', 20000)
b.dispEmployee() 
a.dispInfo() 
b.dispInfo()
print('Base classes from which the Employee class is inherited:', Employee.__base__)
print('The class namespace:', Employee.__dict__)
print('The class name:', Employee.__name__)
print('The module name in which the class is defined:', Employee.__module__)
print('The documentation bar :', Employee.__doc__)



# Create an employee class. Each employee has
# characteristics such as name and salary. The class should
# have a counter that calculates the total number of
# employees, as well as a method that prints the total
# number of employees and a method that displays
# information about each employee in particular, namely
# the name and salary.

# In addition to creating a class, display information
# about the base classes from which the employee
# class is inherited (__base__), the class namespace
# (__dict__), the class name (__name__), the module
# name in which the class is defined (__module__),
# the documentation bar ( __doc__)