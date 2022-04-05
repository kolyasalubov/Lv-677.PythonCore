import re

def correct_tail(body, tail):
    sub = re.findall(f"{tail}$", body)
    if sub:
        return True
    else:
        return False