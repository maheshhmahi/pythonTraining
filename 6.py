import math as m


def euclidian_distance(points):
    distance = 0
    for i1, i2 in points:
        distance = distance + m.pow((i2 - i1), 2)
    res = m.sqrt(distance)
    return res


co_ordinate_points = [(5, 2), (6, 9)]

# co_ordinate_points = [(2,3),(5,6),(11,16)]

res = euclidian_distance(co_ordinate_points)

print(res)
