

class Human():
    def __init__(self, *age):
        self.age = age
        print("The Work of God!")

class Man(Human):
    def __init__(self, *age):
        self.age = age
        super().__init__()
        print("Creation of a man.")
        
class Woman(Human):
    def __init__(self, *age):
        self.age = age
        super().__init__()
        print("The creation of a woman.")


Adam = Man("Adam")
Eve = Woman("Eve")


def God():
    return [Man(), Woman()]

