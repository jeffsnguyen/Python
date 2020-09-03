
# line class lecture

import math

from shapes.point import Point



#Line class
class Line(object): # Point is a class "derived" from object


    def __init__(self, startP, endP): # standard initialization function  x, y coordinate
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




