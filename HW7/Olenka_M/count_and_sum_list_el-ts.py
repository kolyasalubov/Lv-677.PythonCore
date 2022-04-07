def count_positives_sum_negatives(arr: list) -> list:
    if not arr: return []
    else:
        count_positive_el = 0
        sum_negative_el = 0    
        for el in arr:
            if el > 0:
                count_positive_el += 1
            elif el < 0:
                sum_negative_el += el
    return [count_positive_el, sum_negative_el]


