nums = int(input("input number: "))

fibonacci = 1
fibonacci_prev = 0
for i in range(nums-1):
    fibonacci += fibonacci_prev
    fibonacci_prev = fibonacci - fibonacci_prev
    print(fibonacci, end=" ")
