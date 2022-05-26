########## 1
#Count of positives / sum of negatives
# def count_positives_sum_negatives(arr):
#     if not arr:
#         return []
#     else:
#         positives = 0
#         negatives = 0
#         for el in arr:
#             if el > 0:
#                 positives += 1
#             elif el < 0:
#                 negatives += el
#     return [positives, negatives]
#
# arr = [123, 43, 56, 1, 3, 6, -33, -299, -34, 0]
# print(count_positives_sum_negatives(arr))

########## 2
#Reverse List Order
# def reverse_list(l):
#     l.reverse()
#     return l


########## 3
#Multiples of 3 or 5
# def solution(number):
#     sum = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum
# print(solution(25))


########## 4
#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / mpg <= fuel_left
print(zero_fuel(100,25,5))
########## 5
########## 6
########## 7
########## 8
