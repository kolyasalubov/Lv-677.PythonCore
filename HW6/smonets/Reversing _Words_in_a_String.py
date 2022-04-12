def reverse(st):
    words = st.split()
    rev_words = list(reversed(words))
    new_str = ""
    for i in rev_words:
        new_str += str(i)+" "
    return new_str.rstrip()


print(reverse("Hello World."))