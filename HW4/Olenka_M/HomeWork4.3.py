entered_number = int(input("Enter positive integer number or 0 for getting fibonacci numbers ≤ than the entered number: "))

if entered_number == 0:
    print(f"Fibonacci nubber ≤ than entered number {entered_number} is: 0")
elif entered_number < 0:
    print(f"You entered {entered_number}. Fibonacci numbers are not negative numbers. Please, enter positive number or 0")
else:
    fibonacci_numbers = []
    previous_number = 0
    next_number = 1
    fibonacci_numbers.append(previous_number)
    fibonacci_numbers.append(next_number)
    while next_number <= entered_number:
        previous_number = previous_number + next_number
        if previous_number > entered_number:
            break
        fibonacci_numbers.append(previous_number)
        next_number = previous_number + next_number
        if next_number > entered_number:
            break
        fibonacci_numbers.append(next_number)
    print(f"Fibonacci numbers ≤ than entered number {entered_number} are: {fibonacci_numbers}")
