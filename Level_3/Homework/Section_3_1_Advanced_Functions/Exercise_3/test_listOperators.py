# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 3
# Description: Contains the tests for reconcileLists
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
#######################
# Importing necessary packages
from listOperators.listOperators import reconcileLists

#######################


###############################################
def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the reconcileLists method
    #       2. Test reconcileLists using parameters of different type
    #       3. Test reconcileLists with different length lists
    #       4. Test reconcileLists with two empty lists
    ###############################################
    # Test 1.1
    # Scenario: Test reconcileLists using parameters of the same type
    l1 = [1, 3, 5, 7, 9]
    l2 = [1, 3, 5, 8, 10]
    print('Test 1.1')
    print(reconcileLists(l1, l2))
    print()

    # Test 1.2
    # Scenario: Test reconcileLists using parameters of different type
    l1 = [1, 3, 5, 7, 9]
    l2 = [1, 'Los Angeles', 5, 7, 10]
    print('Test 1.2')
    print(reconcileLists(l1, l2))
    print()

    # Test 1.3
    # Scenario: Test reconcileLists with different length lists
    l1 = [1, 3, 5, 7, 9]
    l2 = [1, 'Los Angeles']
    print('Test 1.3')
    print(reconcileLists(l1, l2))
    print()

    # Test 1.3
    # Scenario: Test reconcileLists with two empty lists
    l1 = []
    l2 = []
    print('Test 1.4')
    print(reconcileLists(l1, l2))
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
