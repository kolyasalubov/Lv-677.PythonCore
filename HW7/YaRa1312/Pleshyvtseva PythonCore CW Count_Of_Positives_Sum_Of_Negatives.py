# CodeWars Count_Of_Positives_/_Sum_Of_Negatives

def count_positives_sum_negatives(arr):
    null_list = []
    sum_of_positives = 0
    sum_of_negatives = 0
    if arr == [0, 0] or arr == []:
        return null_list
    for i in arr:
        if i > 0:
            sum_of_positives += 1
        elif i < 0:
            sum_of_negatives += i
        else:
            continue
    return [sum_of_positives, sum_of_negatives]
