#Create a class Human, everyone has a name, create a method in the class that displays a welcome message to a each person.
#  Create a class method in the class that returns information that it is a species of "Homosapiens". 
# And also in the class create a static method that returns an arbitrary message. 

# # Variant - 1
# class Human:
#     def __init__(self, name, age, species):
#         self.name = name
#         self.age = age
#         self.species = species
#     def welcome(self):
#         return (f"Hello, {self.name}")
#     def __str__(self):
#         return (f"{self.name} is {self.species}")

# maximus = Human("Maxim", 22, "Homosapiens")
# print(maximus.welcome())
# print(maximus.__str__())

# Variant 2

class Human():
    species = 'Homosapiens'
    def __init__(self, name):
        self.name = name
    def welcome(self):
        return print(f'Hello, {self.name}')
    @classmethod
    def display(cls):
        return print(f'Human is A species of "{cls.species}"')
    @staticmethod
    def infoMessege(message):
        return print(f'Your massege is - {message}')    

x = Human('Maxim')
x.welcome()
x.display()
x.infoMessege('Glory Ukraine')