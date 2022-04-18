# TTP 8.2

class Employee():
    "The class calculates all the employees and displays information about the employees"
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def employeeNumber(cls):
        return print(f"The number of the employees is {cls.count}")
        
    def employeeInfo(self):
        return print(f"Name: {self.name} \n Salary: {self.salary}")

employee1 = Employee("Iryna", 200)
employee2 = Employee("Natalia", 2000)
employee1.employeeInfo()
employee2.employeeInfo()
Employee.employeeNumber()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
