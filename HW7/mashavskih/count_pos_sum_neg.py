def count_positives_sum_negatives(arr):
    positive_sum = 0
    negative_sum = 0
    if len(arr) == 0:
        return []
    for num in arr:
        if num > 0:
            positive_sum += 1
        elif num < 0:
            negative_sum += num
    return [positive_sum, negative_sum]