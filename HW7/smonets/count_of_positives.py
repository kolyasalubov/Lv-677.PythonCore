def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    result = []
    if arr == []:
        return result
    else:
        for i in arr:
            if i > 0:
                count += 1
            elif i < 0:
                sum += i
        result.append(count)
        result.append(sum)
        return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

count_positives_sum_negatives(arr)