class Employee:
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def total_employees(cls):
        print(f"We have {cls.counter} staff members")

    def employee_info(self):
        print(f"{self.name} has salary of {self.salary} dollars")


artem = Employee("Artem", 322)
alex = Employee("Alex", 480)
artem.employee_info()
alex.employee_info()
Employee.total_employees()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
