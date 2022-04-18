#3.3
user_ineteger_1 = int(input("Enter an integer: "))
user_integer_2 = int(input("Enter an other integer or the same as the first one: "))
def sameOrNot(user_ineteger_1, user_integer_2):
    if (user_ineteger_1 ^ user_integer_2):
        print("Not Same")
    else:
        print("Same")
sameOrNot(user_ineteger_1, user_integer_2)