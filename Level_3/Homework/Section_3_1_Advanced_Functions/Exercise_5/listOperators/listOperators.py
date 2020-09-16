# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 5
# Description: Contains the method reconcileLists
#  The previous exercise presents a good use-case for functools.partial:
#   a. Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute
#       function). Test this comprehensively.
#   b. Create similar partial functions for each of the break* functions in the previous exercise.

# Importing necessary packages

###############################################

# reconcileLists method
# Method to take 2 list as arguments
#   Return a list that has True or False to represent comparison of value between the two if list has the same length
# Modified to take breakFn parameter (a function or lambda) to do additional comparison instead of the original
#   value comparison
def reconcileLists(l1, l2, breakFn):
    # If the list are of the same length:
    #   Via map: pass the callable breakFn on the values from each list--which should return True or False--and return
    #       the mapped object.
    # Else: print an error message and return nothing.
    return list(map(lambda val1, val2: breakFn(val1, val2), l1, l2)) if len(l1) == len(l2) \
        else print('List are not of the same length')


