#https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives

def count_positives_sum_negatives(arr):
    if arr == []: return []
    value = [0,0]
    for i in range(len(arr)):
        if arr[i] > 0: value[0] += 1
        elif arr[i] < 0: value[1] += arr[i]
    return value
