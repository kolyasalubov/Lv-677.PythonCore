print("\n--------------task 2.3 for number ---------------\n")

a = 2
b = 5.5

print("a =", a)
print("b =", b)

print("\n--------------replace vars---------------\n")

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

print("\n--------------task 2.3 for other type---------------\n")

a = "hello"
b = ["world", 2, (1, "hello")]

print("a =", a)
print("b =", b)

print("\n--------------replace vars---------------\n")

""" Якщо існує такий тип даних, до якого можна звести всі інші типи, 
і якщо для цього типу можливі дві протилежні дії, як об'єднання і різниця, 
то можна послідувати попередньому способу"""

""" Або якщо є можливість записати об'єкт в пам'яті без жодного вказівника на нього,
то можна діяти таким способом"""

""" Або якщо є можливість просто поміняти вказівники місцями, однією дією, 
то теж хороший варіант. Бо якщо почерзі, то як я розумію, 
після перенаправлення першого вказівника, об'єкт, на який він вказував перед цим 
стане з лічильником нуль і зникне, тому вже буде неможливо на нього перенаправити другий вказівник"""
print("a =", a)
print("b =", b)