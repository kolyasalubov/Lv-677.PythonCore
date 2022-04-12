zen = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

number_better = zen.find("better")
print("Кількість слів 'better':",number_better)
number_never = zen.find("never")
print("Кількість слів 'never':",number_never)
number_is = zen.find("is")
print("Кількість слів 'is':",number_is)

print(f"Ось весь текст в верхньому регістрі: \n{zen.upper()}")

print(f"Ось весь текст з заміною 'i' на '&': \n{zen.replace('i','&')}")