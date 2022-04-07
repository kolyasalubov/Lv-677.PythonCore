def filter_words(st):
    st = st.lower()
    my_list = list(st.split())
    my_list[0] = my_list[0].capitalize()
    new_str = ""
    for i in my_list:
        new_str += i + " "
    new_str = new_str.rstrip()
    print(new_str)
    return new_str

# def filter_words(st):
#     st = st.lower()
#     st = st.capitalize()
#     print(st)
#     return st
# -------------------------------------------- Чому не працює ? 

string = "WOW this is REALLY amazing OLOLO"

filter_words(string)