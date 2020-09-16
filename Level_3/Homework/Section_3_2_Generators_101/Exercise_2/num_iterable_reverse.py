# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 2
# Description: Contains the tests to reverse iterate through a list of numbers
#   Create a list of 1000 numbers. Convert the list to an reverse iterable and iterate through it.

#######################
# Importing necessary packages
from random import random, seed
#######################


###############################################
def main():

    # Set seed to generate pseudo-random number
    seed(1)
    # Generate list l using list comprehension
    l = [random() for i in range(0, 1000)]

    # Convert to an iterable
    listIter = reversed(l)

    # iterate through list l, Exception Stop Iteration will be raise when it reaches the end of the list.
    while True:
        print(next(listIter))

    ###############################################


#######################
if __name__ == '__main__':
    main()
