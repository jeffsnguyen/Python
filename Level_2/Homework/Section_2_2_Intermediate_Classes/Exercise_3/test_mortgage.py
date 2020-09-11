# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 3
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
from loan.mortgage import MortgageMixin, FixedMortgage, VariableMortgage
#######################


def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the init function of MortgageMixin via FixedMortgage
    #       2. Test the MortgageMixin.PMI() method
    #       3. Test the MortgageMixin.monthlyPayment()method
    #       4. Test the MortgageMixin.principalDue() method
    #   All test will be on a fixed rate mortgage of FixedMortgage
    ###############################################
    # 1. Testing MortgageMixin class
    # Scenario: Assign a MortgageMixin class variable
    # Desire result: Print correct result as assigned
    mortgage1 = FixedMortgage(100000, .050, 30, 100000)
    print('Test block 1: Fixed Rate Mortgage')
    print('Test 1.1')
    print('The mortgage is: ', mortgage1.__repr__())
    print('The mortgage rate is: ', mortgage1.rate())
    print()

    # 2. Testing MortgageMixin.PMI()
    # Scenario: Print out PMI value based on mortgage variable
    # Desire result: Print 0 as current assumption is LTV = 1
    print('Test 1.2')
    print('The PMI value is: ', mortgage1.PMI())
    print()

    # 3. Testing MortgageMixin.monthlyPayment()
    # Scenario: Calculate monthly payment using the overriden MortgageMixin.monthlyPayment() method
    # Desire result: Print correct result
    print('Test 1.3')
    print('The mortgage monthly payment is: ', mortgage1.monthlyPayment())
    print()

    # 4. Testing MortgageMixin.principalDue()
    # Scenario: Calculate principal due using the overriden MortgageMixin.principalDue() method
    # Desire result: Print correct result
    print('Test 1.4')
    print('The mortgage principal due is: ', mortgage1.principalDue(10))
    print()

    # Testing block 2
    # Scenario:
    #   This block will:
    #       1. Test the init function of MortgageMixin via VariableMortgage
    #       2. Test the MortgageMixin.PMI() method via VariableMortgage
    #       3. Test the MortgageMixin.monthlyPayment()method via VariableMortgage
    #       4. Test the MortgageMixin.principalDue() method via VariableMortgage
    #   All test will be on a fixed rate mortgage of FixedMortgage
    ###############################################
    # 1. Testing MortgageMixin class
    # Scenario: Assign a MortgageMixin class variable
    # Desire result: Print correct result as assigned
    mortgage2 = VariableMortgage(100000, {0: .1, 5: .08, 9: .07, 15: .05, 28: .015, 30: .01}, 30, 100000)
    print('Test block 2: Variable Rate Mortgage')
    print('Test 2.1')
    print('The mortgage rate is: ', mortgage2._rateDict)
    print()

    # 2. Testing VariableMortgage.getRate(startPeriod)
    # Scenario: Calculate the variable rate based on passed in startPeriod value
    # Desire result: Print correct result
    print('Test 2.2')
    print('The mortgage rate with the given term is: ', mortgage2.getRate(26))
    print()

    # 3. Testing MortgageMixin.PMI()
    # Scenario: Print out PMI value based on mortgage variable
    # Desire result: Print 0 as current assumption is LTV = 1
    print('Test 2.3')
    print('The PMI value is: ', mortgage2.PMI(26))
    print()

    # 4. Testing MortgageMixin.monthlyPayment()
    # Scenario: Calculate monthly payment using the overriden MortgageMixin.monthlyPayment() method
    # Desire result: Print correct result
    print('Test 2.4')
    print('The mortgage monthly payment is: ', mortgage2.monthlyPayment(26))
    print()

    # 5. Testing MortgageMixin.principalDue()
    # Scenario: Calculate principal due using the overriden MortgageMixin.principalDue() method
    # Desire result: Print correct result
    print('Test 2.5')
    print('The mortgage principal due is: ', mortgage2.principalDue(26))
    print()

    ###############################################
#######################
if __name__ == '__main__':
    main()
