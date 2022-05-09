def count_positives_sum_negatives(arr):
    if not arr:
        return []
    else:
        positives = 0
        negatives = 0
        for el in arr:
            if el > 0:
                positives += 1
            elif el < 0:
                negatives += el
    return [positives, negatives]
