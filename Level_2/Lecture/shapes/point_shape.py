
#class lecture, using derived Shape class

import math
from shapes.base import Shape

# Shape lecture
#class Point(Shape):


class Point(Shape): # Point is a class "derived" from object

    def __init__(self, x=None, y=None): # standard initialization function  x, y coordinate
        # Shape.__init__(self, x=None, y=None) directly invoke the init function on the base Shape class
        # and pass in self. Downside: if base class name change, then every instance of shape needs t be change

        # Better alternative: determine the base class of Point class and call __init__
        # then self is passed to super.
        super(Point, self).__init__()

        self._x = float(x) if x is not None else float(Point._dx) if hasattr(Point, '_dx') else 0
        self._y = float(y) if y is not None else float(Point._dy) if hasattr(Point, '_dy') else 0

    # Default coordinate function
    @classmethod
    def defaultCoordinates(cls, x, y): # Set at the class lvl, 2 coordinates (x,y) as default if not specified
        cls._dx = x # Instead of storing dx, dy at the object lvl, store them at the class lvl
        cls._dy = y # ._dx get values of these variables


    # Can also use @property for cleaner implementation of setX, setY, getX, getY
    # decorator, create a property function
    @property
    def x(self):
        return self._x

    # decorator set x
    @x.setter
    def x(self, ix):
        self._x = ix # Set _x to be input x

    @property
    def y(self):
        return self._y

    # decorator set y
    @y.setter
    def y(self, iy):
        self._y = iy  # Set _x to be input y


    # Creating a class-level method
    @classmethod
    # self refers to object, cls refers to the class
    def distanceCls(cls, pt1, pt2):
        dx = pt1.x - pt2.x
        dy = pt1.y - pt2.y
        return math.sqrt(dx * dx + dy * dy)


    # calculate distance from the object to another object
    # pt refer to another point object
    #def distance(self, pt):
        #dx = self._x - pt._x
        #dy = self._y - pt._y
        #return math.sqrt(dx * dx + dy * dy)

    # Using class method:
    def distance(self, pt):
        return self.distanceCls(self, pt)

    def distanceOrigin(self):
        return self.distance(Point(0,0))

    def toString(self):
        # This overrides the base class <- comment is necessary
        return 'Point(' + str(self._x) + ', ' + str(self._y) + ')'

    def printShape(self):
        # Print the string representation of the Shape object

        # Call the toString function and print it to the screen
        print(self.toString())
