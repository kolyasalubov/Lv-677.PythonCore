class Human():

    species = "Homosapiens" 

    def __init__(self, name):
        self.name = name
    
    def greetings(self):
        print (f'This is {self.name}.')

    def human_species(self):
        print (f' Spesies of {self.name} is {self.species}.')
    
    @staticmethod
    def message():
        print(f'And I wish this Homosapiens a good day!')

charlz = Human('Charlz')
charlz.greetings()
charlz.human_species()
Human.message()
