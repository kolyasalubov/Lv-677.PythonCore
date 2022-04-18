def count_p_n(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []
a = [10, 16, -12, 12, 1, 4, -4, -5]
print(count_p_n(a))