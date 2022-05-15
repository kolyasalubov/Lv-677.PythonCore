my_array = []
 
elements = int(input("Enter number of array elements : "))
 
for variable in range(0, elements):
    value_of_element = int(input("Please input element of array: "))
 
    my_array.append(value_of_element) # adding the element
     
print(f"Your array of inputed elements is: {my_array}")

def new_list():

    positive_count = 0
    negative_count = 0
    num = 0

    while(num < len(my_array)):
      
        if my_array[num] >= 0:
            positive_count += 1
        else:
            negative_count += 1
      
        num += 1

        new_array = []
        new_array2 = []

        sum_negative = sum(i for i in my_array if i < 0)

        new_array.extend((positive_count, sum_negative))
        new_array2.extend((positive_count, negative_count))

    return f"""Array, where the first element is the count of positives numbers and the second element is sum of negative numbers is : {new_array}
Array, where the first element is the count of positives numbers and the second element is the count of negative numbers is : {new_array2}"""

print(new_list())


# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].