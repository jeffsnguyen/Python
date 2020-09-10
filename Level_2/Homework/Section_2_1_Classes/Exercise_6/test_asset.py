# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 6
# Description: This contains the test functions for Exercise 6, Asset class and its methods
#   Create a class called Asset. This class will represent the Asset covered by the loan. The class should
#       do the following:
#       a. Save an initial asset value upon object initialization (i.e. the initial value of a car).
#       b. Create a method that returns a yearly depreciation rate (i.e., 10%).
#       c. Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.
#       d. Create a method that returns the current value of the asset, for a given period. This is the
#           initial value times total depreciation. Total depreciation at time t can be calculated as:
#               (1-monthlyDeprRate)**t

# Importing necessary packages
from asset.asset import Asset
#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the Asset class to see if value is passed correctly.
    #       2. Test monthlyDepr() method
    #       3. Test annualDepr() method
    #       4. Test value(t) method
    ###############################################
    # Test 1
    # Testing Asset
    # Scenario: Initiate an asset value and print result.
    # Desire result: Print correct result as assigned
    print('Test 1')
    asset1 = Asset(1000000)
    print('The asset value entry is:', asset1.__repr__())
    print()

    # Test 2
    # Testing annualDepr()
    # Scenario: Print the annualDepr rate
    # Desire result: Print correct result, i.e. .10
    print('Test 2')
    print('The annual depreciation rate is:', asset1.annualDepr())
    print()

    # Test 3
    # Testing monthlyDepr()
    # Scenario: Calculate and print the monthlyDepr rate form annualRate()
    # Desire result: Print correct result, i.e. .01
    print('Test 3')
    print('The monthly depreciation rate is:', asset1.monthlyDepr())
    print()

    # Test 4
    # Testing value(t)
    # Scenario: Calculate and print the current value if the asset for given period t using value(t)
    #   Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    # Desire result: Print correct result
    print('Test 4')
    t = 10
    print('The current value of the asset at time t=' + str(t) + ' is: ' + str(asset1.value(t)))
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
