'''
Shape class lecture. main file
'''

from shapes.point_shape import Point
from shapes.line_shape import Line

def main():
    pt1 = Point(1,3)
    pt2 = Point(8,7)

    ln = Line(pt1,pt2)

    print(pt1.getID())
    print(pt2.getID())

    print(ln.getID())

    print(pt1.toString())
    print(pt2.toString())
    print(ln.toString())

#######################
if __name__ == '__main__':
    main()