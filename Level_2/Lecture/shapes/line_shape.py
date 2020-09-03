
# line class lecture, using derived Shape

import math

from shapes.point import Point
from shapes.base import Shape


#Line class
class Line(Shape): # Point is a class "derived" from object


    def __init__(self, startP, endP): # standard initialization function  x, y coordinate
        super(Line, self).__init__()
        self._startP = startP
        self._endP = endP

    @property
    def startP(self):
        return self._startP

    @startP.setter
    def startP(self, istartP):
        self._startP = istartP

    @property
    def endP(self):
        return self._endP

    @endP.setter
    def endP(self, iendP):
        self._endP = iendP

    def length(self):
        return self._startP.distance(self._endP)

    def toString(self):
        return 'Line(' + self._startP.toString() + ', ' + self._endP.toString() + ')'


