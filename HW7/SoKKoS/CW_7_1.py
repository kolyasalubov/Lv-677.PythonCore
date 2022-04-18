def count_positives_sum_negatives(arr):
    first_element_array = 0
    second_element_array = 0
    newarray = [0, 0]
    null_array = []
    if arr == [0, 0] or arr == []:
        return null_array
    for i in arr:
        if i > 0:
            first_element_array += 1
            newarray[0] = first_element_array
        elif i < 0:
            second_element_array = second_element_array + i
            newarray[1] = second_element_array
        else:
            continue
    return newarray


array_xxx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(array_xxx))