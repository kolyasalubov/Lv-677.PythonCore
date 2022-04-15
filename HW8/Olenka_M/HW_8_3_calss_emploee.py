class Employee:
    """ Class Employee was created for work with information about employee`s salary and for counting all employees"""
    counter = 0
    def __init__(self, name: str, salary: float):
        Employee.counter += 1
        self.name = name
        self.salary = salary
    
    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def total_number (cls):
        print(f"Total employee number is {cls.counter}")

    def employee_info(self):
        print(f"Employee {self.name} has salary {self.salary}")

employee1 = Employee("Ihor", 455.55)
employee2 = Employee("Svitlana", 500)
employee1.employee_info()
Employee.total_number()
    
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)