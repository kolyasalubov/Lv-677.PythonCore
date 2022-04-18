start = 0
finish = 100
while start < finish:
    print(start, end=" ")
    start += 2

#############################################

for num in range(100):
    if num % 2 != 0:
        print(num, end=" ")

##############################################

for num in range (1,101,2):
    print(num, end=" ")

###############################################
num = [24,23,43,56,65,78,90,77]
for num in (num):
    if num % 2 == 0:
        continue
    print(num)

###############################################
start = 1
finish = 100
while start < finish:
    print(start, end=" ")
    start += 2


##############################################

num = int(input("Enter you number:"))
for num in range(num):
    if num % 2 == 0:
        continue
    print(num end=" ")
