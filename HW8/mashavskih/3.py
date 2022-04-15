class Employee():
    count = 0
    def __init__(self, name, salary ):
        self.name = name
        self.salary = salary
        Employee.count +=1
    def dispEmployee(self):
        return print(f'There are {Employee.count} employee in dpt.')

    def dispInfo(self):
        return print(f'Name: {self.name}\nSalary: {self.salary}')

a =Employee('Mary', 30000)
b =Employee('Mike', 20000)
b.dispEmployee() 
a.dispInfo() 
b.dispInfo()
print('Base classes from which the Employee class is inherited:', Employee.__base__)
print('The class namespace:', Employee.__dict__)
print('The class name:', Employee.__name__)
print('The module name in which the class is defined:', Employee.__module__)
print('The documentation bar :', Employee.__doc__)
