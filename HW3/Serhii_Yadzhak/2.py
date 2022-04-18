num = input('Enter the number: ' )
x = [int(a) for a in str(num)]
print(x)
answer = 1
for i in x:
    answer *= i
print(answer)
print(list(reversed(x)))
print(list(sorted(x)))