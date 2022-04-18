import re

def reverse(st):
    
    st = re.sub(' +', ' ', st)
    st = st.strip()
    list = st.split(' ')
    
    return ' '.join(word for word in list[::-1])
