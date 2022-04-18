#https://www.codewars.com/kata/is-this-my-tail/train/python

def correct_tail(body, tail):
    sub = len(body)
    n = 0
    for i in body:
        n += 1
        if n == sub and i == tail: return True
    return False
