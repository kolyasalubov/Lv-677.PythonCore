
class Employee():

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary
    
    def __del__(self):
        Employee.counter -=1
    
    @classmethod
    def employees_total(cls):
        print('Total number of employees is:', Employee.counter)

    def employee_info(self):
        print (f'Name of employee is: {self.name} and salary equal to {self.salary} m.u.') 

karl = Employee('Karl', 300)
klara = Employee('Klara', 300)
john = Employee('John', 300)

print(Employee.employees_total())
john.employee_info()