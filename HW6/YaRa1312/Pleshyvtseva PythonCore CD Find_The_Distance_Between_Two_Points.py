# CodeWars Find_The_Distance_Between_Two_Points

def distance(x1, y1, x2, y2):
    result = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(result, 2)
