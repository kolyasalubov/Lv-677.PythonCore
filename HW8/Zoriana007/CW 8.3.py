def double_char(word:str):

    out = []

    for letter in word:
        out.append(letter + letter)

    return "".join(out)

print(double_char("God Fod"))



# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "