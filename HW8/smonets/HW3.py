class Employee():
    """
    Creates Employee
    You must provide Employee name (str) and salary (num).

    """
    counter = 0

    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = int(salary)
         
    def __new__(self, *args, **kwargs):
        self.counter += 1
        return object.__new__(self)
        
    @classmethod
    def total_emp(cls):
        print(f"We have {cls.counter} employees in total")
        
    def emp_info(self):
        print(f"This is {self.name}, his salary is {self.salary} $")
        
    
s = Employee("Sviat", 9999)
o = Employee("Oleg", 99999)
g = Employee("Anna", 3333)
        
o.emp_info()
g.emp_info()
o.total_emp()

# print(Employee.__doc__)
# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
