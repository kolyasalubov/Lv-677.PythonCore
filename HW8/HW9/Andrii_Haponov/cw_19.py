# Color Ghost
# Create a class Ghost

# Ghost objects are instantiated without any arguments.

# Ghost objects are given a random color attribute 
# of "white" or "yellow" or "purple" or "red" when instantiated

# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"

# Цветной призрак
# Создайте класс Ghost

# Объекты-призраки создаются без каких-либо аргументов.

# Объектам-призракам при создании экземпляра присваивается случайный атрибут 
# цвета «белый», «желтый», «фиолетовый» или «красный».
import random

class Ghost(object):       
    def __init__(self, color = ["white", "yellow", "purple", "red"]):
        self.color = random.choice(color)
       

ghost = Ghost()
print(ghost.color)
