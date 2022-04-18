# Task3. Write a function that calculates the number of characters included in a given string
# input: “hello”
# output: {“h”:1, “e”:1, “l”:2, “o”:1}

def counts(func):
    output_list = (input_list)
    counts = {}
    for i in output_list:
        counts[i] = input_list.count(i)
    return counts
input_list = input("Enter your string:  ")
print(f'Output {counts(input_list)}')