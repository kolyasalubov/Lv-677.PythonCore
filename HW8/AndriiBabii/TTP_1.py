#Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to a each person. 
# Create a class method in the class that 
# returns information that it is a species of "Homosapiens". 
# And also in the class create a static method that returns an arbitrary message. 

class Human():

    def __init__(self, human_name):
        self.name = human_name
        pass

    def welcome(self):
        print(f"{self.name}, hello!")

    @classmethod
    def species(cls):
        return "Homosapiens"
    
    @staticmethod
    def who_is():
        return """
        Humans (Homo sapiens) are the most abundant and widespread species of primate, 
        characterized by bipedalism and large, complex brains. 
        This has enabled the development of advanced tools, culture, and language. 
        Humans are highly social and tend to live in complex social structures 
        composed of many cooperating and competing groups, 
        from families and kinship networks to political states. 
        """


doctor_octopus = Human("Gunther")
doctor_octopus.welcome()
print(Human.species())
print(Human.who_is())

