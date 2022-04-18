number_four_significant = 3256
number_1 = str (number_four_significant)
result = 1
for c in number_1:
    result *=int(c) 
print(result)

print (number_1[::-1])

sort_number = sorted(number_1)
sort_numberstr = ''.join(sort_number)
print(sort_numberstr)