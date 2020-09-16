# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 5
# Description: Contains the tests for:
#   breakAbsolute,
#   breakRelative,
#   breakAbsRelative,
#   reconcileLists
# The previous exercise presents a good use-case for functools.partial:
#   a. Create a partial called reconcileListsBreakAbsolute (which uses the breakAbsolute
#       function). Test this comprehensively.
#   b. Create similar partial functions for each of the break* functions in the previous exercise.
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

    # Testing block 1
    # Scenario:
    #   This block will:
    #       A. Test the breakAbsolute stored lambda method
    #       B. Test the breakRelative stored lambda method
    #       C. Test the breakAbsRelative stored lambda method
    #       1. Test the modified reconcileLists method with breakAbsolute as breakFn
    #       2. Test the modified reconcileLists method with breakRelative as breakFn
    #       3. Test the modified reconcileLists method with breakAbsRelative as breakFn
    ###############################################

    # Test A
    # A. Test the breakAbsolute stored lambda method
    print('Test A: Test the breakAbsolute stored lambda method')
    print(breakAbsolute(5, 4, 1))
    print(breakAbsolute(5, 1, 2))
    print(breakAbsolute(500, 400, 20))
    print()

    # Test B
    # B. Test the breakRelative stored lambda method
    print('Test A: Test the breakRelative stored lambda method')
    print(breakRelative(5, 4, 1))
    print(breakRelative(5, 1, 2))
    print(breakRelative(500, 400, 20))
    print()

    # Test C
    # C. Test the breakAbsRelative stored lambda method
    print('Test C: Test the breakAbsRelative stored lambda method')
    print(breakAbsolute(5, 4, 1))
    print(breakAbsolute(5, 1, 2))
    print(breakAbsolute(500, 400, 20))
    print()

    # Test 1.1
    # Scenario: Test the modified reconcileLists method with breakAbsolute as breakFn
    print('Test 1.1: Test the modified reconcileLists method with breakAbsolute as breakFn')
    print('Test 1.1.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    print(reconcileLists(l1, l2, partial(breakAbsolute, epsilon=1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 1.1.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 0, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakAbsolute, epsilon=10)))
    print()

    # Test 1.2
    # Scenario: Test the modified reconcileLists method with breakRelative as breakFn
    print('Test 1.2: Test the modified reconcileLists method with breakRelative as breakFn')
    print('Test 1.2.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    print(reconcileLists(l1, l2, partial(breakRelative, percent=1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 1.2.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 10, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakRelative, percent=10)))
    print()

    # Test 1.3
    # Scenario: Test the modified reconcileLists method with breakAbsRelative as breakFn
    print('Test 1.3: Test the modified reconcileLists method with breakAbsRelative as breakFn')
    print('Test 1.3.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]
    print(reconcileLists(l1, l2, partial(breakAbsRelative, percent=1)))
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 1.3.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 20, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    print(reconcileLists(l1, l2, partial(breakAbsRelative, percent=10)))
    print()
    ###############################################

    # Testing block 2
    # Scenario:
    #   This block will:
    #       1. Test the reconcileListsBreakAbsolute partial method
    #       2. Test the reconcileListsBreakRelative partial method
    #       3. Test the reconcileListsBreakAbsRelative partial method
    ###############################################

    # Test 2.1
    # Scenario: Test the reconcileListsBreakAbsolute partial method which utilizes breakAbsolute
    print('Test 2.1: Test the reconcileListsBreakAbsolute partial method which utilizes breakAbsolute')
    print('Test 2.1.1: This should yield the same result as test 1.1.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]

    # reconcileListsBreakAbsolute method
    # Method that return a list of boolean value comparing elements of list l1 and l2
    #   using partial breakAbsolute method
    reconcileListsBreakAbsolute = list(map(lambda val1, val2: partial(breakAbsolute, epsilon=1)(val1, val2), l1, l2))

    print(reconcileListsBreakAbsolute)
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 2.1.2: This should yield the same result as test 1.1.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 0, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    reconcileListsBreakAbsolute = list(map(lambda val1, val2: partial(breakAbsolute, epsilon=10)(val1, val2), l1, l2))
    print(reconcileListsBreakAbsolute)
    print()

    # Test 2.2
    # Scenario: Test the reconcileListsBreakRelative partial method which utilizes breakRelative
    print('Test 2.2: Test the reconcileListsBreakRelative partial method which utilizes breakRelative')
    print('Test 2.2.1: This should yield the same result as test 1.2.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]

    # reconcileListsBreakRelative method
    # Method that return a list of boolean value comparing elements of list l1 and l2
    #   using partial breakRelative method
    reconcileListsBreakRelative = list(map(lambda val1, val2: partial(breakRelative, percent=1)(val1, val2), l1, l2))

    print(reconcileListsBreakRelative)
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 2.2.2: This should yield the same result as test 1.2.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 10, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    reconcileListsBreakRelative = list(map(lambda val1, val2: partial(breakRelative, percent=10)(val1, val2), l1, l2))
    print(reconcileListsBreakRelative)
    print()

    # Test 2.3
    # Scenario: Test the reconcileListsBreakAbsRelative partial method which utilizes breakAbsRelative
    print('Test 2.3: Test the reconcileListsBreakAbsRelative partial method which utilizes breakAbsRelative')
    print('Test 2.3.1: This should yield the same result as test 1.3.1')
    l1 = [-1, 10, 5, 7, 9, -1, 10, 5, 7, 9, -1, 10, 5, 7, 5, 7, 9, -1, 10, 5, 9, -1, 10, 5, 7, 9]
    l2 = [0, 10, 8, 10, 5, 5, 8, 0, 5, 10, 0, 5, 5, 5, 8, 10, 0, 5, 5, 8, 10, 0, 5, 5, 8, 10]

    # reconcileListsBreakAbsRelative method
    # Method that return a list of boolean value comparing elements of list l1 and l2
    #   using partial breakAbsRelative method
    reconcileListsBreakAbsRelative = list(map(lambda val1, val2: partial(breakAbsRelative, percent=1)(val1, val2), l1, l2))

    print(reconcileListsBreakAbsRelative)
    # Redo test with new set of lists
    print('Redo test with new set of lists')
    print('Test 2.3.2: This should yield the same result as test 1.3.2')
    l1 = [-7, 111, 14, 1, 5, -7, 1, 9, 4, 6, -1, 20, 1, 46, 22, 23, 12, -15, 156, 3, 1, 2, 3, 4, 6, 8]
    l2 = [12, 1, 14, 0, 5, 5, 3, 7, 8, 30, 35, 24, 26, 68, 45, 23, 12, 57, 12, 14, 87, 14, 15, 76, 34, 11]
    reconcileListsBreakAbsRelative = list(map(lambda val1, val2: partial(breakAbsRelative, percent=10)(val1, val2), l1, l2))
    print(reconcileListsBreakAbsRelative)
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
