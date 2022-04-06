def create_array(n: float) -> list:
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res

def create_array(n: float) -> list:
    return [i for i in range(1, n+1)]
    