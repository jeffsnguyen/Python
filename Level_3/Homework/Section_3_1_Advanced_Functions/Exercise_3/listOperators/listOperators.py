# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 3
# Description: Contains the method reconcileLists
#  Create a regular function (called reconcileLists) that takes two separate lists as its parameters. In this example:
#
#   List 1 represents risk valuations per trade (i.e. Delta) from Risk System A and List 2 has
#       the same from Risk System B. The purpose of this function is to reconcile the two lists and report the
#       differences between the two systems. To this end, it should return a list of True or False values,
#       corresponding to each value in the lists (True means they match at index, False means they don’t
#       match at index).
#
#   Test the reconcileLists function with different lists of values (lists should be of at least length ten).
#   Note that the assumption is that both lists are the same length (report an error otherwise).
# Importing necessary packages

###############################################
# Method to take 2 list as arguments
#   Return a list that has Tru or False to represent comparison of value between the two if list has the same length
def reconcileLists(l1, l2):
    # If the list are of the same length:
    #   Via map: pass the comparison of each value from each list--which should return True or False--and return
    #       the mapped object.
    # Else: print an error message and return nothing.
    return list(map(lambda val1, val2: val1 == val2, l1, l2)) if len(l1) == len(l2) \
        else print('List are not of the same length')


###############################################
