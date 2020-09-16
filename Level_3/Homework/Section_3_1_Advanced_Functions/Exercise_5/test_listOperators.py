# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 4
# Description: Contains the tests for breakAbsolute, breakRelative, breakAbsRelative, reconcileLists
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

#######################
# Importing necessary packages
from listOperators.listOperators import reconcileLists
from functools import partial
#######################


###############################################
def main():
    # Stored lambda methods
    ###############################################
    # breakAbsolute stored lambda method
    # Method to take 2 values and an epsilon parameter as arguments
    #   Return 'True' if two values are not within epsilon of each other
    breakAbsolute = lambda val1, val2, epsilon: abs(val1 - val2) > abs(epsilon)

    # breakRelative stored lambda method
    # Method to take 2 values and a percent parameter as arguments
    #   Return 'True' if the percent difference between the two values exceeds percent
    breakRelative = lambda val1, val2, percent: ((val1 - val2) / val1) * 100 > percent

    # breakAbsRelative stored lambda method
    # Method to take 2 values and a percent parameter as arguments
    #   Return 'True' if the percent difference between the absolute values of the two values exceeds percent.
    breakAbsRelative = lambda val1, val2, percent: ((abs(val1) - abs(val2)) / abs(val1)) * 100 > percent
    ###############################################



    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the breakAbsolute stored lambda method
    #       2. Test the breakRelative stored lambda method
    #       3. Test the breakAbsRelative stored lambda method
    #       4. Test the modified reconcileLists method with breakAbsolute as breakFn
    #       5. Test the modified reconcileLists method with breakRelative as breakFn
    #       6. Test the modified reconcileLists method with breakAbsRelative as breakFn
    ###############################################

    # Test 1.4
    # Scenario: Test the modified reconcileLists method with breakAbsolute as breakFn
    print('Test 1.4: Test the modified reconcileLists method with breakAbsolute as breakFn')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    reconcileListsBreakAbsolute = partial
    print(reconcileLists(l1, l2, partial(breakAbsolute, 1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 0, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakAbsolute, 10)))
    print()

    # Test 1.5
    # Scenario: Test the modified reconcileLists method with breakRelative as breakFn
    print('Test 1.5: Test the modified reconcileLists method with breakRelative as breakFn')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    print(reconcileLists(l1, l2, partial(breakRelative, 1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 0, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakRelative, 10)))
    print()

    # Test 1.6
    # Scenario: Test the modified reconcileLists method with breakAbsRelative as breakFn
    print('Test 1.6: Test the modified reconcileLists method with breakAbsRelative as breakFn')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    print(reconcileLists(l1, l2, partial(breakAbsRelative, 1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 0, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakAbsRelative, 10)))
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
