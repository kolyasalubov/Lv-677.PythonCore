def distance(x1, y1, x2, y2):
    "Test string"
    distance_btw_points = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(distance_btw_points,2)