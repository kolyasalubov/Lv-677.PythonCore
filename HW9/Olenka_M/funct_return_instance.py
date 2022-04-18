class Human():
    def __init__(self):
        super().__init__()
class Man(Human):
    def __init__(self):
        super().__init__()
class Woman(Human):
    def __init__(self):
        super().__init__()
    
adam = Man()
eve = Woman()

def God():
    return [adam, eve]

#Saw version below at codewars. It`s simpler ... LOL:
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]