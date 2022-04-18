# CodeWars No_Yelling!

def filter_words(st):
    st = st.lower()
    user_list = list(st.split())
    user_list[0] = user_list[0].capitalize()
    string = ""
    for i in user_list:
        string += i + " "
    string = string.rstrip()
    return string

st = input("Enter a string: ")
print(filter_words(st))
