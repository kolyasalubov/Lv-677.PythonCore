divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_and_3 = []
divisible_by_2.append([i for i in range(1, 11) if i % 2 == 0])
divisible_by_3.append([i for i in range(1, 11) if i % 3 == 0])
not_divisible_by_2_and_3.append([i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0])
print(divisible_by_2)
print(divisible_by_3)
print(not_divisible_by_2_and_3)