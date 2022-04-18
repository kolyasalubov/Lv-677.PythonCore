entered_n = int(input('Enter number n: '))
fib = [0, 1]
while len(fib) <= entered_n:
    fib.append(fib[-2]+fib[-1])
print(fib)