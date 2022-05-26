# Create an Create an employee class. Each employee has characteristics such as name and salary. 
# The class should have a counter that calculates the total number of employees, as well as a method 
# that prints the total number of employees and a method that displays information about each employee 
# in particular, namely the name and salary.

class Employee_salary:
    """ 
    The Employee class counts the employees and their salary
    """
    amount = 0
    def __init__(self, name: str, salary: float):
        Employee_salary.amount += 1
        self.name = name
        self.salary = salary
    
    def __del__(self):
        Employee_salary.amount -= 1

    @classmethod
    def total_number (cls):
        print(f"Total employee number is {cls.amount}")

    def employee_info(self):
        print(f"Employee {self.name} has salary {self.salary} hryvnia")

employee_1 = Employee_salary("Mykyta", 26500)
employee_2 = Employee_salary("Oksana", 25000)
employee_1.employee_info()
employee_2.employee_info()
Employee_salary.total_number()

print(Employee_salary.__base__)
print(Employee_salary.__dict__)
print(Employee_salary.__name__)
print(Employee_salary.__module__)
print(Employee_salary.__doc__)
