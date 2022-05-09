first_num = 1
second_num = 1

n = int(input())

print(first_num, second_num, end=" ")
for i in range(2, n):
    first_num, second_num = second_num, first_num + second_num
    print(second_num, end=" ")
input()
