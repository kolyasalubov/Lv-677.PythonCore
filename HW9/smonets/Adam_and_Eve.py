class Human():
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        super().__init__()
        
class Woman(Human):
    def __init__(self):
        super().__init__()

def God():
    Man1 = Man()
    Woman1 = Woman()
    paradise = (Man1, Woman1)
    return paradise
