import math 

def distance(x1, y1, x2, y2):
    """
    Given two ordered pairs calculate the distance between them. 
    Round to two decimal places. 
    """
    return round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0),2)