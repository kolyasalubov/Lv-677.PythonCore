print("_________________________________________version 0____________________________________________")
import random as r
class Ghost(object):
    def __init__(self):    
        self.color = r.choice(["white", "yellow", "purple", "red"])



#print("_________________________________________version 1____________________________________________")
# import random as r
# class Ghost(object):      
#     def __init__(self):
#         i = r.randint(0,3)
#         colors = ["white", "yellow", "purple", "red"]
#         self.color = colors[i]

# ghost = Ghost()
# print(ghost.color)

ghosts = [Ghost().color for _ in range(100)]
print(ghosts)
