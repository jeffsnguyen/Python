# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 2
# Description: Contains the tests of WAR_mortgage, WAM_mortgage
#  This exercise is a modification of Exercise 1.5.8, to use the reduce function. In Exercise 1.5.8, we
#       created functions to calculate the WAM and WAR of a list of mortgage tuples.
#   a. Create an alternate version of WAM, which takes a list of mortgage tuples; for this version,
#       use the reduce function, with a regular function as its callable, to calculate the WAM.
#   b. Create an alternate version of WAR, which takes a list of mortgage tuples; for this version,
#       use the reduce function, with a lambda as its callable, to calculate the WAR of the list of rates.
#   c. Modify your WAR and WAM functions in your LoanPool class to take the above reduce
#       approach instead of the previous approach.
#######################
# Importing necessary packages
from mortgage.mortgage_WARWAM import WAR_mortgage, WAM_mortgage

#######################

###############################################
def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the WAR_mortgage method
    #       2. Test the WAM_mortgage method
    ###############################################
    # Generate list
    p = [(523000, .030, 360), (270000, .030, 200), (932000, .045, 350)]

    # Test 1.1
    # Scenario: Test the WAR_mortgage method to calculate Weighted Average Rate using lambda function
    print('Test 1.1')
    print('The Weighted Average Rate is: ', WAR_mortgage(p))
    print()

    # Test 1.2
    # Scenario: Test the WAM_mortgage method to calculate Weighted Average Maturity using lambda function
    print('Test 1.2')
    print('The Weighted Average Maturity is: ', WAM_mortgage(p))
    print()

    ###############################################


#######################
if __name__ == '__main__':
    main()
