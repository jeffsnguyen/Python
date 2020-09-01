
#class lecture

import math

#Point class
class Point(object): # Point is a class "derived" from object
    def __init__(self, x, y): # standard initialization function  x, y coordinate
        self._x = float(x) # create var inside the class call _x and save x value to ._x
        self._y = float(y) # _x is a protected variable, should not be access outside

    # Variables can be accessed from outside using custom function set and get

#    def setX(self, x):
#        self._x = x #every function the class has to have self

#    def setY(self, y):
#        self._y = y

#    def getX(self):
#        return self._x

#    def getY(self):
#        return self._y

    # Can also use @property for cleaner implementation of setX, setY, getX, getY
    # decorator, create a property function
    @property
    def x(self):
        return self._x


    # decorator set x
    @x.setter
    def x(self, ix):
        self._x = ix # Set _x to be input x

    # calculate distance from the object to another object
    # pt refer to another point object
    def distance(self, pt):
        dx = self._x - pt._x
        dy = self._y - pt._y
        return math.sqrt(dx * dx + dy * dy)

    def distanceOrigin(self):
        return self.distance(Point(0,0))

