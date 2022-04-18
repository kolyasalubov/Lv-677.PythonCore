import random

colors = ["white", "yellow", "purple", "red"]
class Ghost():
    def __init__(self):
        self.color = colors[random.randint(0,3)]
        pass
    
a = Ghost()
ghosts = [Ghost().color for _ in range(100)]
print(ghosts)