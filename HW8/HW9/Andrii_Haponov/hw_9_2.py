# 72
# Create a class Human, everyone has a name, create a method 
# n the class that displays a welcome message to a each person. Create a class method 
# in the class that returns information that it is a species of "Homosapiens". 
# And also in the class create a static method that returns an arbitrary message. 

# Создайте класс Human, у каждого есть имя, создайте в классе метод, 
# который отображает приветственное сообщение для каждого человека. 
# Создайте метод класса в классе, который возвращает информацию о том, что это вид «Homosapiens». 
# А также в классе создать статический метод, возвращающий произвольное сообщение.

class Human():

    def method(self):
        return f"Hello, {self}!"
    
    @classmethod
    def classmethod(cls):
        return "This species is of 'Homosapiens'.", cls

    @staticmethod
    def staticmethod():
        return "In the class create a static method."

obj1 = Human()
obj2 = Human()
# print(Human.method(obj1))
print(obj1.method())
print(obj2.method())
print(Human.classmethod())
print(obj1.classmethod())
print(obj1.staticmethod())
print(obj2.staticmethod())

