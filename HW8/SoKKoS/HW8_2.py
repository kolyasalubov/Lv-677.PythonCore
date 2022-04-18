class Human:
    def method(self):
        return print(f'Hello - {self}')

    @classmethod
    def classmethod(cls):
        return print('it is a species of "Homo sapiens"')

    @staticmethod
    def staticmethod():
        return print('Congratulations')





name_human = input('Enter your name: ')
Human.method(name_human)
Human.classmethod()
Human.staticmethod()

