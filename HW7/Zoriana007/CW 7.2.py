print("Now we will need to create our own list to reverse it using created by us function.")

my_list = []

n = int(input("Please input how many items should be in a list: "))

for i in range(0,n):
    value = int(input("Please input element of a list: "))
    my_list.append(value)
    
print(my_list)

def reverse_list():
    
    new_list = my_list[::-1]
    
    return new_list
    
print(f"Reversed list is: {reverse_list()}")



# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]