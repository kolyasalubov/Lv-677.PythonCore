def word_count(text):
    """
    This function counts amount
    of each given symbol
    in the text
    """
    count = {}
    for c in set(text):
        count[c] = text.count(c)
    return count

text_count = input("Put the text: ")
print(word_count(text_count))