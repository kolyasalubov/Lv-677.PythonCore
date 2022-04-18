Zen='''Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''
replaced_zen1=Zen.replace('.',' ')
replaced_zen2=replaced_zen1.replace(',',' ')
Zen_of_python=list(replaced_zen2.split(' '))
number1 = 0
for i in Zen_of_python:
    if i == 'better':
        number1 += 1
number2 = 0
for i in Zen_of_python:
    if i == 'never':
        number2 += 1
number3 = 0
for i in Zen_of_python:
    if i == 'is':
        number3 += 1
print('Number of words better: ', number1)
print('Number of words never: ', number2)
print('Number of words is: ', number3)
print(Zen.upper())
print(Zen.replace('i','&'))