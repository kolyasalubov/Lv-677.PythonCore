def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive_array_count = 0
    negative_array_count = 0
    neither_array = 0
    for i in arr:
        if i > 0:
            positive_array_count = positive_array_count + 1
        elif i == 0:
            neither_array = neither_array + i
        else:
            negative_array_count = negative_array_count + i 

    return [positive_array_count, negative_array_count]