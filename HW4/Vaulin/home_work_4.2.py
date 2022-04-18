# Lv-677.PythonCore

## Home Work 3.2
#Task2. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
#(Hint: use the built-in float () function).

nowiy_list = []
list_1 = [24, 13, 28, 53]
for m in list_1:
    nowiy_list.append(float(m))
print (nowiy_list)

# Time to practice №1
# Print all even numbers less than 100 (write two variants of the code: 
# one using the while loop, 
# and 
# the other using the for loop). 

# number = 100
# for n in range(1, 102):
#     if n % 2 == 0:
#         print(n)

# Time to practice №2

# number = 100
# for n in range(1, 100):
#     if n % 2 == 0:
#         continue
#     else:
#         print(n)

# Time to practice №3

# bro = [17, 11, 34 , 84, 52]
# for x in bro:
#     if x % 2 == 0:
#         print (x)
#         break