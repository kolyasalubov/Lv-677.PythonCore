#https://www.codewars.com/kata/basic-subclasses-adam-and-eve

class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        super().__init__()

class Woman(Human):
    def __init__(self):
        super().__init__()

def God():
    m = Man()
    w = Woman()
    res = [m,w]
    return res

