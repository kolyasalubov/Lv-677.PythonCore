a = int(input('Please, write number A: '))
b = int(input('Please, write number B: '))
sign = input('Sign +, -, *, /, **:')
if sign == '+':
     print(a + b)
elif sign == '-':
     print(a - b)
elif sign == '*':
     print(a * b)
elif sign == '**':
     print(a ** b)
elif sign == '/' :
     if b != 0:
          print(a / b)
     else:
          print('Divide by 0!')