def count_positives_sum_negatives(arr):
    list = []
    count = 0
    negative = 0
    if len(arr) == 0:
        return []
    for x in arr:
        if x > 0:
            count += 1
        elif x < 0:
            negative += x
    return [count, negative]