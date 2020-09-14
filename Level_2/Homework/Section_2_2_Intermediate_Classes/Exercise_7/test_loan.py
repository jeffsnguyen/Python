# Type: Homework
# Level: 2
# Section: 2.2: Intermediate
# Exercise: 6
# Description: This contains the Asset class and its methods
#   This exercise focuses on creating the individual Asset derived classes. Do the following:
#       a. Modify the annualDeprRate method of the Asset class to trigger a not-implemented error.
#           This ensures that no one can directly instantiate an Asset object (makes it abstract).
#       b. Create a Car class, derived from Asset. Derive multiple car types from Car (i.e. Civic, Lexus,
#           Lamborghini, etc.). Give each one a different depreciation rate.
#       c. Create a HouseBase class, derived from Asset. Derive PrimaryHome and VacationHome
#           from House. Give each one a different depreciation rate (note, a vacation home will
#           depreciate slower than a primary home since it is often vacant).

# Importing necessary packages
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
from loan.mortgage import MortgageMixin, FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the __init__ function of Loan in the base loan class.
    #       2. Test the __init__ function of MortgageMixin
    #       3. Test the PMI() function of MortgageMixin with LTV based on asset value instead of loan's notional value
    #       4. Test the __init__ function of AutoLoan
    #       5. Test the recoveryValue function of Loan
    #       6. Test the equity function of Loan
    #
    ###############################################
    # Test 1.1
    # Scenario: Test the __init__ function of Loan in the base loan class.
    #   The __init__ method will only works if the asset parameters is from the Asset family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    print('Test 1.1')
    asset1 = Asset(1000000)
    car1 = Car(100000)
    loan1 = Loan(100000, .05, 30, asset1)
    loan1 = Loan(100000, .05, 30, car1)
    print()

    # Uncomment to test
    #loan1 = Loan(100000, .05, 30, 'This aint it chief')

    # Test 1.2
    # Scenario: Test the __init__ function of MortgageMixin
    #   The __init__ method will only works if the home parameters is from the HouseBase family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    print('Test 1.2')
    car1 = Car(1000000)
    car2 = Lambourghini(1000000)
    housebase1 = HouseBase(1000000)
    primaryhome1 = PrimaryHome(100000)
    vacayhome1 = VacationHome(100000)
    mortgage1 = FixedMortgage(100000, .05, 30, housebase1)
    mortgage1 = FixedMortgage(100000, .05, 30, primaryhome1)
    mortgage1 = FixedMortgage(100000, .05, 30, vacayhome1)

    # Uncomment to test
    #mortgage1 = FixedMortgage(100000, .05, 30, car1)
    print()

    # Test 1.3
    # Scenario: 3. Test the PMI() function of MortgageMixin with LTV based on asset value
    #               instead of loan's notional value
    print('Test 1.3')
    print('The PMI value is: ', mortgage1.PMI(20))
    print()

    # Test 1.4
    # Scenario: 4. Test the __init__ function of AutoLoan
    #   The __init__ method will only works if the car parameters is from the Car family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    print('Test 1.4')
    autoloan1 = AutoLoan(100000, .05, 30, car1)
    autoloan2 = AutoLoan(100000, .05, 30, car2)
    # Uncomment to test
    #autoloan1 = AutoLoan(100000, .05, 30, vacayhome1)
    print()

    # Test 1.5
    # Scenario: 5. Test the recoveryValue function of Loan
    #   The recoveryValue method will return the current asset value for the given period
    #       times a recovery multiplier of .6
    print('Test 1.5')
    print('The asset value for the given period is: ', autoloan1.recoveryValue(20))
    print('The asset value for the given period is: ', mortgage1.recoveryValue(20))
    print()

    # Test 1.6
    # Scenario: 6. Test the equity function of Loan
    #   The equity method will return the available equity (current asset value less current loan balance)
    print('Test 1.6')
    print('The current available equity is: ', mortgage1.equity(20))
    print('The current available equity is: ', autoloan2.equity(20))
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
