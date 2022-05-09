class Human:
    species = "homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}")

    @classmethod
    def person_species(cls):
        return f"Your species is {cls.species}"

    @staticmethod
    def static_massage():
        return "Today is a good day"


character = Human("Alex")
character.welcome()
print(character.person_species())
print(character.static_massage())
