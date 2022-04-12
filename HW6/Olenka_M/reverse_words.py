def reverse(st:str) -> str:
    st = st.split()
    st = " ".join(st[::-1])
    
    return st


def reverse(st:str) -> str:
    st = [word for word in st.split()[::1]]
    st = " ".join(st)
    
    return st
