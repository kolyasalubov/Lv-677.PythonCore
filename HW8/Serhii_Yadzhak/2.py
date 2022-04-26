class Human:
    human = 'homosapien'
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f'Hallo, {self.name}')
    @classmethod
    def homosapiens(cls):
        print(f'human is {cls.human}')
    @staticmethod
    def arbitrary(latin):
        print(f'Homo sapiens, {latin} the species to which all modern human beings belong')

t=Human('Anton')
t.welcome()
t.homosapiens()
t.arbitrary('(Latin: “wise man”)')