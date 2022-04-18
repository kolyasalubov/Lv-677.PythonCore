import re

def filter_words(st):
    st = re.sub(' +', ' ', st)
    st = st.strip()
    st = st.lower()
    st = st.capitalize()
    return st
