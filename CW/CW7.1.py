def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    my_array = []
    if arr == []:
        return my_array
    else:
        for i in arr:
            if i > 0:
                count += 1
            elif i < 0:
                sum += i
        my_array.append(count)
        my_array.append(sum)
    return my_array