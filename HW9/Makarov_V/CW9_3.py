class Human:
    def __init__(self):
        super().__init__()


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


def god():
    adam = Man()
    eve = Woman()
    first = (adam, eve)
    return first
