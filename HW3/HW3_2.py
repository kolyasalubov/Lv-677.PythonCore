from audioop import reverse


number = input("Please, input a 4-digit number ")
num_composition = int(str(number[0])) * int(str(number[1])) * int(str(number[2])) * int(str(number[3])) 
print (num_composition)

num_reverse = list(reversed(number))
print (num_reverse)

num_sort = sorted
print (num_sort)
