
#class lecture

import math

#Point class

#class Point(object): # Point is a class "derived" from object
#    def __init__(self, x, y): # standard initialization function  x, y coordinate
#        self._x = float(x) # create var inside the class call _x and save x value to ._x
#        self._y = float(y) # _x is a protected variable, should not be access outside

    # Variables can be accessed from outside using custom function set and get

#    def setX(self, x):
#        self._x = x #every function the class has to have self

#    def setY(self, y):
#        self._y = y

#    def getX(self):
#        return self._x

#    def getY(self):
#        return self._y

class Point(object): # Point is a class "derived" from object

    #_dx = 0
    #_dy = 0

    def __init__(self, x=None, y=None): # standard initialization function  x, y coordinate
        # Use x,y value if it's not empty, otherwise use Point._dx, Point._dy
        #self._x = float(x) if x is not None else float(Point._dx) #not self._dx because we want to access the class lvl
        #self._y = float(y) if y is not None else float(Point._dy)

        ## Alternative
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

