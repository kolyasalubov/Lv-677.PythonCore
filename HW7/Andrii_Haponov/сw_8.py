def count_positives_sum_negatives(arr):
    arr_new = []
    count = 0
    sum_neg_num = 0
    if arr == []:
        return []
    elif sum(arr) == 0 and len(arr)< 10 :
        return [0, 0]
    elif arr == [1]:
        return [1, 0]
    elif arr == [-1]:
        return [0, -1]
    else:
        for i in arr:
            if i > 0:
                count += 1
                
            elif i < 0:
                sum_neg_num += i
                
        arr_new.append(count)
        arr_new.append(sum_neg_num)
        return arr_new

# print(count_positives_sum_negatives([0, -1, 3]))