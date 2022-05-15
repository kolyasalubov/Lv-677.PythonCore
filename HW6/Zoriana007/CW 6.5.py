def reverse(st:str):
    reversed_word = st.split()
    
    reversed_word.reverse()
    
    print(" ".join(reversed_word))
    
    return reversed_word

reverse("Animal is a lion")




# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# Example (Input --> Output)

# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"