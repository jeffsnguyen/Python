'''
class lecture
'''

from shapes.point import Point


def main():
    #pt = Point(1,4) # call the init function and create a Point object
    #print(pt.getX())
    #print(pt.getY())

    #pt.setX(4.9)
    #print(pt.getX())

    # pt2 = Point(8, -3)
    # print(pt.distance(pt2))

    #print(pt.distanceOrigin())

    #print(pt.x)

    #pt.x = 5.5

    #print(pt.x)

    #pt1 = Point(5,4)
    #pt2 = Point(-2,5)

    #print(Point.distanceCls(Point(5,4), Point(-2,5)))

    #pt = Point(8,9)
    #print(pt.distance(Point(5,6)))

    pt = Point()
    print(pt.x)
    print(pt.y)

    Point.defaultCoordinates(4,6)

    pt2 = Point()
    print(pt2.x)
    print(pt2.y)

#######################
if __name__ == '__main__':
    main()