class Employee:
    """ Create an Create an employee class. Each employee has characteristics such as name and salary.
    The class should have a counter that calculates the total number of employees, as well as a method
    that prints the total number of employees and a method that displays information about each employee
    in particular, namely the name and salary."""
    count = 0

    def __init__(self, name: str, salary: float):
        Employee.count += 1
        self.name = name
        self.salary = salary

    @classmethod
    def total_num(cls):
        print(f"Total employee number is {cls.count}")

    def info(self):
        print(f"Employee {self.name} has salary {self.salary}")


employee1 = Employee("Sidorov", 122)
employee2 = Employee("Ivanov", 100)
employee3 = Employee("Scvorcov", 133)
employee1.info()
employee2.info()
employee3.info()

Employee.total_num()

print(f"__base__ {Employee.__base__}\n")
print(f"__dict__ {Employee.__dict__}\n")
print(f"__name__ {Employee.__name__}\n")
print(f"__module__ {Employee.__module__}\n")
print(f"__doc__ {Employee.__doc__}\n")