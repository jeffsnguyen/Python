'''
class lecture
'''

from shapes.point import Point


def main():
    pt = Point(1,4) # call the init function and create a Point object
    #print(pt.getX())
    #print(pt.getY())

    #pt.setX(4.9)
    #print(pt.getX())

    pt2 = Point(8, -3)
    print(pt.distance(pt2))

    print(pt.distanceOrigin())

    print(pt.x)

    pt.x = 5.5

    print(pt.x)

#######################
if __name__ == '__main__':
    main()