# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "



def double_char(s):
    dubl_s = ""
    for i in s:
        n = i * 2
        dubl_s += n
    return dubl_s

print(double_char("String"))