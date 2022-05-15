def number_of_letters(word:str):
    result = {}
    for letter in word:
        result[letter] = word.count(letter)
    print(result)
    return result

number_of_letters("Zoriana")

# Task3. 
# Write a function that calculates the number of characters included in a given string:
# input: "hello"
# output: {"h":1, "e":1,"l":2,"o":1}