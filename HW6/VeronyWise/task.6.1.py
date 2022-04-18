def bigger_number(number_1, number_2):
     '''
     Function that returns the largest number of two numbers 
     '''
     if number_1 > number_2:
          return (f" {number_1} the largest number")
     elif number_1 < number_2:
          return (f" {number_2} the largest number")
     else:
          return (f"The number 1 {number_1} is the same the number 2 {number_2}")

number_1 = float(input("Write number 1: "))
number_2 = float(input("Write number 2: "))
print(bigger_number(number_1, number_2))

