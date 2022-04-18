class Employee:
    count = 0
    def __init__(self, name, salary):
        Employee.count += 1
        self.name = name
        self.salary = salary
    @classmethod
    def counters(cls):
        return print(f"Employee count =  {cls.count}")

    def total_members(self):
        return print(f"This is {self.name}. And his/her salary is {self.salary}")

michal = Employee("Michal", 1800)
ivan = Employee("Ivan", 1800)
# print(ivan.total_members())
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)