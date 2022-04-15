class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_massage(self):
        print(f"Welcome dear {self.name}")
            
    @classmethod
    def species_of_Human(cls):
        return f"Species is {cls.species}"

    @staticmethod
    def static_massage():
        return "Be happy!"

someone = Human("John")
someone.welcome_massage()
print(Human.species_of_Human())
print(Human.static_massage())
