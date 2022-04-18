first_number=int(input('Enter the first number of list: '))
last_number=int(input('Enter the last number of list: '))
elements_of_integer = list(range(first_number, last_number+1))
for i in elements_of_integer:
  print(float(i))