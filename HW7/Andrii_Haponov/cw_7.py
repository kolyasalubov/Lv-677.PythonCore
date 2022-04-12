# Count of positives / sum of negatives

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and 
# the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    count = 0
    sum_negativ_num = 0
    arr_new =[]
    if arr == []:
        return arr_new
    else:
        for i in arr:
            if i > 0:
                count += 1
                arr_new = arr_new.append[count]
            elif i == 0:
                arr_new = arr_new.append[i]       
            else:
                sum_negativ_num += i
                arr_new = arr_new.append[sum_negativ_num]           
        return arr_new

print(count_positives_sum_negatives(input("Eneter list: ")))