
# line class lecture
# This module contains the Shape class



# Shape class
class Shape(object): # Point is a class "derived" from object

    _id = 0

    # Assign every id a shape
    # id to start from 0, everyh time an object is create, id is incremented
    def __init__(self): # no parameters necessary because there is nothing specific to a shape

        # create id based on the class level id + 1
        # self._id is the object lvl id, shape._id is the class lvl id
        self._id = Shape._id + 1
        # only affect the id at the class lvl and not the object lvl
        # next time another shape object is created, id will be incremeted
        Shape._id += 1


    def getID(self):
        return self._id

    def toString(self):
        # Every derived Shape should have an implemented toString() function
        # This is so that input has the form of Point(1,[space]3)
        # for the toString function to describ ethe object using a string

        # because it is a base class, so there is no need to implement string
        raise NotImplementedError()

    def printShape(self):
        # Print the string representation of the Shape object

        # Call the toString function and print it to the screen
        print(self.toString())





