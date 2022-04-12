print("\n--------------task 2.1---------------\n")

# Version 0. Scroll down to version 1

# import this, codecs
# get_zen = codecs.decode(this.s, 'rot13')
# zen = f"{get_zen}"
# print("----------------------------------------------")
# print(zen)


# zen_words = zen.split()

# count_better = 0
# count_never = 0
# count_is = 0

# for word in zen_words:
#     if word == "better":
#         count_better += 1    

# for word in zen_words:
#     if word == "never":
#         count_never += 1    

# for word in zen_words:
#     if word == "is":
#         count_is += 1    

# print(count_better)
# print(count_never)
# print(count_is)

# zen_upper = zen.upper()
# print(zen_upper)

# zen_ampersand = zen.replace("i", "&")

# Version 0 end

print("\n----------------Version 1----------------\n")

# Version 1

import this, codecs
get_zen = codecs.decode(this.s, 'rot13')

#zen = ("%s" % get_zen)
#zen = "{}".format(get_zen)
zen = f"{get_zen}"

print("----------------------------------------------\n")
#print(zen)


zen_words = zen.split()

count_better = zen_words.count("better")
count_never = zen_words.count("never")
count_is = zen_words.count("is")

print('Quantity "better" in zen of Phython is:', count_better)
print('Quantity "never" in zen of Phython is:', count_never)
print('Quantity "is" in zen of Phython is:', count_is)

print("----------------------------------------------\n")

zen_upper = zen.upper()
print(zen_upper)

zen_ampersand = zen.replace("i", "&")
#print(zen_ampersand)
