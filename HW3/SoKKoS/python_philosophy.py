import this, codecs

zen_string = codecs.encode(this.s, 'rot13')
print("\nвходжень слова better - ", zen_string.count("better"))
print("входжень слова never - ", zen_string.count("never"))
print("входжень слова is - ", zen_string.count("is"), "\n")
print("Далі текст у верхньому регістрі\n")
print(f"{zen_string.upper()}\n")
print("Замінити всі входження символу “і” на “&”\n")
print(zen_string.replace("i", "&"))

