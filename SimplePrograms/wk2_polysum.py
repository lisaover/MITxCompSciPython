from math import pi, tan
def polysum(n, s):
    '''
    n: the number of sides of the regular polygon
    s: the length of the side of the regular polygon
    
    returns: sum of the area and square of the perimeter of the regular polygon
    '''
    area = (0.25*n*(s**2))/(tan(pi/n))
    perim_sq = (n*s)**2
    
    return round(area + perim_sq, 4)

n = 5
s = 3
print(polysum(n, s))
