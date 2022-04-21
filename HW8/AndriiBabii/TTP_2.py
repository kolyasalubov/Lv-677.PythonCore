# Create an employee class. 
# Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees,
#  as well as a method that prints the total number of employees and a method that
#   displays information about each employee in particular, namely the name and salary.

# In addition to creating a class, 
# display information about the base classes 
# from which the employee class is inherited (__base__), 
# the class namespace (__dict__), the class name (__name__), 
# the module name in which the class is defined (__module__), the documentation bar ( __doc__) 

class Employee():
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def amount(cls):
        return print(f"Amount of the employees: {cls.count}")
        
    def info(self):
        return print(f"Name: {self.name}\nSalary: {self.salary}")

emp1 = Employee("Ivan", 200)
emp2 = Employee("Taras", 2000)
emp1.info()
emp2.info()
Employee.amount()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)