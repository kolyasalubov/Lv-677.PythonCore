def summation(num):
    return int(num * (num+1) / 2)


number = int(input('The number will always be a positive integer greater than 0.'))

print(f'summation = {summation(number)}')

