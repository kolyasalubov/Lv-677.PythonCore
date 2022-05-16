import random as random
color = ["white","yellow","purple","red"]
class Ghost(object):
    def __init__(self):
        i = random.randint(0,3)
        self.color = color[i]

ghosts = [Ghost().color for _ in range(100)]
print(ghosts)