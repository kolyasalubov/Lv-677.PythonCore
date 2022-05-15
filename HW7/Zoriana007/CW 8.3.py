def calcs (number):
    
    sum = 0
    
    for variable in range (1,number):
        # sum of all the multiples of 3
        if variable % 3 == 0:
            sum += variable
        # sum of all the multiples of 5
        elif variable % 5 == 0:
            sum += variable
        # sum of all the multiples of 3 or 5
        elif variable % 5 and variable % 5 ==0:
            continue
    return sum

print(calcs(88))




# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)
               
    
