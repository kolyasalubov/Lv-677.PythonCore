# Создайте класс Ball. Объекты мяча должны принимать один аргумент
#  для «типа мяча» при создании экземпляра.

# Если аргументы не указаны, объекты мяча должны создаваться с «типом мяча» «обычный».

# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

class Ball(object):
    # ball_type = "regular"
    """This is my first class"""
    def __init__(self, ball_type = "regular" ):
        self.ball_type = ball_type


ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)       
print(ball2.ball_type) 



