def product_num(num):  
    product = 1  
    for n in str(num):
        product *= int(n)
    return int(product)

def reverse_num(num):    
    return int(str(num)[::-1])

def sort_num(num):    
    list = [int(n) for n in str(num)]
    list.sort()
    return int(''.join(str(n) for n in list))


number = 2431
print(product_num(number))
print(reverse_num(number))
print(sort_num(number))
