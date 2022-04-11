def count_positives_sum_negatives(arr):
    lst = []  
    lst.append(sum(1 for x in arr if x > 0))
    lst.append(sum(x for x in arr if x < 0))
    if len(arr) == 0:
        return []
    return lst