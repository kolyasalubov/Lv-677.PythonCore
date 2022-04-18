#var 1
div1 = [num for num in range(1, 11) if num % 2 != 0 and num % 3 != 0]
print(f"Not divisible by 2 and 3: {div1}")

div2 = [num for num in range(1, 11) if num % 2 == 0]
print(f"Divisible by 2: {div2}")

div3 = [num for num in range (1, 11) if num % 3 == 0]
print(f"Divisible by 3: {div3}")
input()
#var 2

for num in range(1, 11):
    if num % 2 == 0:
        print("Divisible by 2: ", num)
    elif num % 3 == 0:
        print("Divisible by 3: ", num)
    elif num % 2 != 0 and num % 3 != 0:
        print("Not divisible by both: ", num)
input()
