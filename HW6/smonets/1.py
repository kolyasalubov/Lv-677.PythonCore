def largest_num(num1, num2):
    """ returns largers number of two numbers """
    if num1 > num2:
        return num1
    else:
        return num2
    

print(largest_num(10, 999))

largest = lambda x,y: x if x > y else y

print(largest(10, 333))
