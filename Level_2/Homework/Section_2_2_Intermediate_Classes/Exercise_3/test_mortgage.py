# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 3
# Description: This contains tests for MortgageMixinclass methods
#   Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate base class(es)

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
    mortgage1 = MortgageMixin(100000, .050, 30, 100000)
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
