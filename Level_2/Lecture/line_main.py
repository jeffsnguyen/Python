'''
line class lecture. main file
'''

from shapes.point import Point
from shapes.line import Line

def main():
    pt1 = Point(3,4)
    pt2 = Point(9,6)

    ln = Line(pt1, pt2)

    ln2 = Line(Point(9,-4), Point(-8,3))

    print(ln.length())
    print(ln2.length())

#######################
if __name__ == '__main__':
    main()