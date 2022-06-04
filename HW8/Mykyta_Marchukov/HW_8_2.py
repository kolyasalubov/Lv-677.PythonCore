# Create a class Human, everyone has a name, create a method in the class that displays a welcome message
# to a each person. Create a class method in the class that returns information that it is a species
# of "Homosapiens". And also in the class create a static method that returns an arbitrary message. 

class Human():

    species = "Homosapiens" 

    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print (f'Hello, {self.name}!!')

    def human_species(self):
        print (f'Spesies of {self.name} is {self.species}.')
    
    @staticmethod
    def message():
        print(f'His serves in ZSU.')

person = Human('Kolya')
person.greeting()
person.human_species()
Human.message()