# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 2
# Description: This contains test for MortgageMixin class methods.
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
from loan.mortgage import MortgageMixin
#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the init function of MortgageMixin
    #       2. Test the MortgageMixin.PMI() method
    #       3. Test the MortgageMixin.monthlyPayment()method
    #       4. Test the MortgageMixin.principalDue() method
    ###############################################
    # 1. Testing MortgageMixin class
    # Scenario: Assign a MortgageMixin class variable
    # Desire result: Print correct result as assigned
    mortgage1 = MortgageMixin(100000, .050, 30, home=100000)
    print('Test 1')
    print('The mortgage is: ', mortgage1.__repr__())
    print()

    # 2. Testing MortgageMixin.PMI()
    # Scenario: Print out PMI value based on mortgage variable
    # Desire result: Print 0 as current assumption is LTV = 1
    print('Test 2')
    print('The PMI value is: ', mortgage1.PMI())
    print()

    # 3. Testing MortgageMixin.monthlyPayment()
    # Scenario: Calculate monthly payment using the overriden MortgageMixin.monthlyPayment() method
    # Desire result: Print correct result
    print('Test 3')
    print('The mortgage monthly payment is: ', mortgage1.monthlyPayment())
    print()

    # 4. Testing MortgageMixin.principalDue()
    # Scenario: Calculate principal due using the overriden MortgageMixin.principalDue() method
    # Desire result: Print correct result
    print('Test 4')
    print('The mortgage principal due is: ', mortgage1.principalDue(10))
    print()
    ###############################################
#######################
if __name__ == '__main__':
    main()
