def distance(x1, y1, x2, y2):
    result = round(((x2 - x1)**2 + (y2 - y1)**2)**(1/2),2)
    print (result)
    return result

distance(1,1,0,0)



# Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.