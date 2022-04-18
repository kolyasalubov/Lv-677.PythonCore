# TTP 8.1

class Human():
    species = 'Homosapiens'
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return print(f"Hello, {self.name}")
    @classmethod
    def information(cls):
        return print(f'Humans are speciec of "{cls.species}"')
    @staticmethod
    def message(message):
        return print(f"The message: {message}")

iryna = Human("Iryna")
iryna.greeting()
iryna.information()
iryna.message("Glory to Ukraine!")
