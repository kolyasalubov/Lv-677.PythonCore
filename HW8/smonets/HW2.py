class Human():
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
        
    def welcome(self):
        print(f"Hello, {self.name} !")
        
    @classmethod
    def species_info(cls):
        print(f"Human is species of {cls.species}")
    
    @staticmethod
    def text(msg):
        print(msg)
        
s = Human("Sviat")

s.welcome()

s.species_info()

s.text("ololo")
