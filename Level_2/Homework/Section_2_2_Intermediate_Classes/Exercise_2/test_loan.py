# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 2
# Description: This contains Loan class methods: FixedRateLoan, VariableRateLoan, getRate
#   Create a MortgageMixin class which will contain mortgage-specific methods. In particular, we’d like
#       to implement the concept of Private Mortgage Insurance (PMI). For those unaware, PMI is an extra
#       monthly payment that one must make to compensate for the added risk of having a Loan-to-Value
#       (LTV) ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
#   To this end, implement a function called PMI that returns 0.0075% of the loan face value, but only if
#       the LTV is < 80%. For now, assume that the initial loan amount is for 100% of the asset value.
#   Additionally, override the base class monthlyPayment and principalDue functions to account for
#       PMI (Hint: use super to avoid duplicating the formulas, and note that the other methods
#       (interestDue, balance, etc.) should not require any changes).

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
    loan2 = VariableRateLoan(100000, {0: .1, 30: .01, 5: .08, 9: .07, 15: .05, 28: .015}, 30)
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
    print('The Variable Rate of is: ', loan2.getRate(26))
    ###############################################
#######################
if __name__ == '__main__':
    main()
