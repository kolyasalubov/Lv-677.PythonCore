word_of_calculate = str(input("Enter world:"))
result_of_count = {}

for i in word_of_calculate:
    if i in result_of_count:
        result_of_count[i] = result_of_count[i] + 1
    else:
        result_of_count[i] = 1

print(result_of_count)