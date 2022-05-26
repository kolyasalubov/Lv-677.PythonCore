################# 1
#Simple: Find The Distance Between Two Points
# def distance(x1, y1, x2, y2):
#     return round((((x1 - x2)**2 + (y1 - y2)**2)**0.5), 2)


################# 2
#No yelling!
# def filter_words(st):
#     st = st.lower()
#     user_list = list(st.split())
#     user_list[0] = user_list[0].capitalize()
#     string = ""
#     for i in user_list:
#         string += i + " "
#     string = string.rstrip()
#     return string
#
# st = "heLLo   WOrld!"
# print(filter_words(st))


################# 3
# Unfinished Loop - Bug Fixing #1
# def create_array(n):
#     res=[]
#     i=1
#     while i<=n:
#         res+=[i]
#         i+=1
#     return res


################# 4
#Convert a Number to a String!
# def number_to_string(num):
#     return str(num)
# print(number_to_string(123))


################# 5
#Reversing Words in a String
def reverse(st):
    words = st.split()
    rev_words = list(reversed(words))
    new_str = ""
    for i in rev_words:
        new_str += str(i)+" "
    return new_str.rstrip()


print(reverse("Hello World asdasd."))