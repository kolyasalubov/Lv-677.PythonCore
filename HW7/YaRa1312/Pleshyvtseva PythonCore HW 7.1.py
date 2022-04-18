#7.1

#from math import pow
#from math import pi

import module2_user_choice_between_r_t_c

print(module2_user_choice_between_r_t_c.user_choice_between_rectangle_triangle_circle())


# user_choice = input("What area you would like to count (1 - rectangle, 2 - triangle, 3 - circle)? ")
# if user_choice == "1":
#     a = int(input("Enter length value: "))
#     b = int(input("Enter width value: "))
#     print(r_t_c_areas.rectangle_area(a, b))
# elif user_choice == "2":
#     a = int(input("Enter length value of a side to which the high is drawn: "))
#     h = int(input("Enter a length value of a high that is drawn to the side 'a': "))
#     print(r_t_c_areas.triangle_area(a, h))
# elif user_choice == "3":
#     r = int(input("Enter a radius value: "))
#     print(r_t_c_areas.circle_area(r))
# else:
#     print("Error, try again")


# def rectangle_area(a, b):
#     '''
#     The function calculates a rectangle area
#     based on user length and width parameters.
#     It can also calculate a quadrant area.
#     '''
#     rect_area = a * b
#     return(f"The rectangle area is {rect_area}")

# def triangle_area(a, h):
#     '''
#     The function calculates a triangle area
#     based on user parameteres (length value
#     of a side and a length value of a high
#     that is drawn to the mentioned side).
#     '''
#     trian_area = 0.5*a*h
#     return(f"The triangle area is {trian_area}")

# def circle_area(r):
#     '''
#     The function calculates a circle area
#     based on user parameter (length of radius).
#     Pi is written to within 11 characters
#     after the comma.
#     '''
#     circ_area = pi * pow(r, 2)
#     return(f"The circle area is {circ_area}")
