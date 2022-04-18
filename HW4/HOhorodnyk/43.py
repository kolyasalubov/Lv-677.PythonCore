number_for_stop = int(input("Enter number when count stop:"))

a, b, c, = 0, 1, 0

if number_for_stop <= 0:
    print('Please enter number greater than 0')
for f in range(0 ,number_for_stop):
    a = b
    b = c
    c = a + b

    print(c, end=' ')
