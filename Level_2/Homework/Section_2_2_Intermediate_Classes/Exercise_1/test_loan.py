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
from loan.loans import FixedRateLoan, VariableRateLoan
from loan.loan_base import Loan
#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the rate function of the class FixedRateLoan to see if it returns rate correctly
    #       2. Test the __init__ function of VariableRateLoan and its ability to check attribute type
    #       3. Test the rate function of VariableLoan to see if it returns period-specific rate correctly
    ###############################################
    # 1. Testing FixedRateLoan
    # Scenario: Assign a FixedRateLoan (child of Loan) variable.
    # Desire result: Print correct result as assigned
    loan1 = FixedRateLoan(100000, .050, 30)
    print('Test 1')
    print('The Fixed Rate is:', loan1.rate())
    print()

    # 2. Testing VariableRateLoan
    # Scenario: Assign a child VariableRateLoan (child of Loan) variable.
    #   In this case, the rate is a dict.
    # Desire result: Print correct result as assigned
    loan2 = VariableRateLoan(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30)
    print('Test 2')
    print('The Variable Rate is:', loan2.__repr__())
    print()

    # 3. Testing VariableRateLoan
    # Scenario: Assign a child VariableRateLoan (child of Loan) variable.
    #   In this case, the passed-in rate of loan2 is not a dict
    # Desire result: Display a TypeError
    print('Test 3')
    loan2 = VariableRateLoan(100000, .050, 30)
    loan2.getRate
    print()

    # 4. Testing VariableRateLoan, getRate(period) method
    # Scenario: Assign a child VariableRateLoan (child of Loan) variable.
    #   In this case, the rate dict is a proper dict.
    #   User call getRate with a passed-in period value to look up the correct interest rate.
    # Desire result: Look up and display the correct interest rate. The correct rate is the one in the rateDict
    #   corresponded to the period just before the lookup period value. For example: for 17 period lookup value, the
    #   correct interest rate to be used for {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01} is 15, not 28.
    print('Test 4')
    loan2 = VariableRateLoan(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30)
    print('The Variable Rate is: ', loan2.getRate(26))
    ###############################################
#######################
if __name__ == '__main__':
    main()
