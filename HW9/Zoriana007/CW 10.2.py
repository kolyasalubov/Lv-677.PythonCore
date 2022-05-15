import random

colors = ["white", "yellow", "purple", "red"]
class Ghost():
    def __init__(self):
        self.color = colors[random.randint(0,3)]
        pass
    
a = Ghost()
ghosts = [Ghost().color for _ in range(100)]
print(ghosts)



# Color Ghost
# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"