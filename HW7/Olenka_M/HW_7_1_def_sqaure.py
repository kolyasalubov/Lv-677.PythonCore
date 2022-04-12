def rectangle_square(side_a: float, side_b: float) -> float:
    """
    Function returns square of rectangle if we have two adjacent sides of one, 
    which are measured in the same units
    """
    return side_a*side_b

def triangle_square(side_a: float, height_a: float) -> float:
    """
    Function returns square of triangle if we have side of one and height drawn to this side, 
    which are measured in the same units.
    The first argument is the side.
    The second argument is the height.
    """
    return 1/2*(side_a*height_a)

def circle_square(radius: float) -> float:
    """Function returns square of circle if we radius, rounted to 2 points"""
    from math import pi as PI
    from math import pow
    return round(pow(radius,2) * PI, 2)