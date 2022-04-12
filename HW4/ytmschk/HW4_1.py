number = int(input('Enter your number: '))
fact_list = []
fact = 1

while number != 0:
    fact_list.append(number)
    number -= 1
for x in fact_list:
    fact *= x

print (fact)