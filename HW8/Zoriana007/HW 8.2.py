class Human():
     
     def __init__(self, name):
         self.name = name

     def welcome_message(self):
          print(f'Hello, {self.name}')

     def method(self):
          print(f'You are Homosapiens {name}.')

     @staticmethod
     def staticmethod():
        print('Its static method.')

name = input("Write your name: ")
obj_name = Human(name)
obj_name.method()
obj_name.staticmethod()


# Create a class Human, everyone has a name, create
# a method in the class that displays a welcome
# message to a each person. Create a class method in
# the class that returns information that it is a species
# of "Homosapiens". And also in the class create a
# static method that returns an arbitrary message.