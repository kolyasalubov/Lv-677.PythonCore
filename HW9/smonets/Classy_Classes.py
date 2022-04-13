class Person():
    def __init__(self,name,age):
        self.name = str(name)
        self.age = int(age)
        self.info=f"{self.name}s age is {self.age}"
        
        
a = Person("Sviat", 30)

print(a.info)
    