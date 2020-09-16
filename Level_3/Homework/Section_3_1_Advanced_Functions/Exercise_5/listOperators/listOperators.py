# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 4
# Description: Contains the method reconcileLists
#  To incorporate lambda into the previous exercise, do the following:
#
#       a. Create a breakAbsolute stored lambda which takes two values and an epsilon parameter.
#           This lambda should ‘return’ True if the two values are not within epsilon of each other.
#
#       b. Create a breakRelative stored lambda which takes two values and a percent parameter. This
#           lambda should ‘return’ True if the percent difference between the two values exceeds percent.
#
#       c. Create a breakAbsRelative function which takes two values and a percent parameter. This
#           should return True if the percent difference between the absolute values of the two values exceeds percent.
#
#       d. Modify the reconcileLists function to take a third parameter, called breakFn (this represents
#           a passed-in function or lambda). The reconcileLists function should utilize the passed-in
#           breakFn function to build the True/False list. You will need to use functools.partial to
#           specify the parameter of the breakFn function (i.e., epsilon or percent).
#
#       e. Test reconcileLists with different lists of values (should be large lists of numbers) and with
#           each of the above break* functions.

# Importing necessary packages


###############################################

# reconcileLists method
# Method to take 2 list as arguments
#   Return a list that has Tru or False to represent comparison of value between the two if list has the same length
# Modified to take breakFn parameter (a function or lambda) to do additional comparison instead of the original
#   value comparison
def reconcileLists(l1, l2, breakFn):
    # If the list are of the same length:
    #   Via map: pass the callable breakFn on the values from each list--which should return True or False--and return
    #       the mapped object.
    # Else: print an error message and return nothing.
    return list(map(lambda val1, val2: breakFn(val1, val2), l1, l2)) if len(l1) == len(l2) \
        else print('List are not of the same length')

###############################################
