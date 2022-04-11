import module1_r_t_c_areas

def user_choice_between_rectangle_triangle_circle():
    '''
    The function allows a user to chose
    a figure between a rectangle, a triangle
    and a circle to calculate its area.
    '''
    user_choice = input("What area you would like to count (1 - rectangle, 2 - triangle, 3 - circle)? ")
    if user_choice == "1":
        a = int(input("Enter length value: "))
        b = int(input("Enter width value: "))
        print(module1_r_t_c_areas.rectangle_area(a, b))
    elif user_choice == "2":
        a = int(input("Enter length value of a side to which the high is drawn: "))
        h = int(input("Enter a length value of a high that is drawn to the side 'a': "))
        print(module1_r_t_c_areas.triangle_area(a, h))
    elif user_choice == "3":
        r = int(input("Enter a radius value: "))
        print(module1_r_t_c_areas.circle_area(r))
    else:
        print("Error, try again")
