class Human():
    species = 'Homosapiens'
    def __init__(self, name_of_user):
        self.name_of_user = name_of_user
    def dispMathod(self):
        return print(f'Hello, {self.name_of_user}')
    @classmethod
    def infoMathod(cls):
        return print(f'Human it is a species of "{cls.species}"')
    @staticmethod
    def infoMessege(message):
        return print(f'Your massege is - {message}')    

s = Human('Mary')
s.dispMathod()
s.infoMathod()
s.infoMessege('Hello Ukraine')
