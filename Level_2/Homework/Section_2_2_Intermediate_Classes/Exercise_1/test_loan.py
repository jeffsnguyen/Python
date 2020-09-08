# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 1
# Description: This contains the test function for the Exercise 1: FixedRateLoan, VariableRateLoan, getRate
#   As shown in the lecture, create derived classes as follows:
#       a. A FixedRateLoan class which derives from Loan.
#       b. A VariableRateLoan class which derives from Loan. This will differ from a FixedRateLoan in
#           that it has a rate dict instead of a single rate value. This dict will contain startPeriod as key
#           and rate as value. This should have its own __init__ function that does the following:
#               i. Validates that the rate parameter is indeed a dict (if not, print an error).
#               ii. Invokes the super-class’ __init__ function with all the parameters.
#
#           The result of the above is that a VariableRateLoan's _rate attribute, as well as its rate
#           property getters/setters will be a dict instead of a value. However, the functions that use
#           the rate (i.e. balance) does not yet know how to handle a dict of rates. To handle this, do the
#           following:
#               i. Create a getRate function in the base Loan class. This should take a period
#                   parameter. and return the result of the rate property.
#               ii. Override the getRate function in VariableRateLoan. This version will calculate the
#                   rate from the dict based on the period argument. Tip: Keep in mind that the dict
#                   only contains startPeriod for each rate -- the code will need to infer the rate for any
#                   period in between.
#
#           Then, modify the Loan class functions (i.e. balance) to use the getRate function to get the
#           rate for the current period.
#
#           Note that the monthly payment and balance formulas are technically different in this
#           Variable case, but we will avoid changing it for simplicity (the focus of the remaining
#           exercises and case study are on fixed rate loans only).

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
    # Testing Asset
    # Scenario: Initiate an asset value and print result.
    # Desire result: Print correct result as assigned
    asset1 = Asset(1000000)
    print('The asset value entry is:', asset1.__repr__())

    # Testing annualDepr()
    # Scenario: Print the annualDepr rate
    # Desire result: Print correct result, i.e. .10
    print('The annual depreciation rate is:', asset1.annualDepr())

    # Testing monthlyDepr()
    # Scenario: Calculate and print the monthlyDepr rate form annualRate()
    # Desire result: Print correct result, i.e. .01
    print('The monthly depreciation rate is:', asset1.monthlyDepr())

    # Testing value(t)
    # Scenario: Calculate and print the current value if the asset for given period t using value(t)
    #   Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    # Desire result: Print correct result
    t = 10
    print('The current value of the asset at time t=' + str(t) + ' is: ' + str(asset1.value(t)))

    ###############################################


#######################
if __name__ == '__main__':
    main()
