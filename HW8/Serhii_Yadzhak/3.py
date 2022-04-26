class Employee():
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    @classmethod
    def totalnumber(cls):
        print(f'Total number of employee {cls.counter}')
    def info(self):
        print(f'Name of employee {self.name} with salary {self.salary}.')   
