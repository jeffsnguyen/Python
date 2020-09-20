# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains exception handling test for Loan classes
#   Add logging statements to your Loan class. This should consist of the following:
#       a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the
#           initialization function), log an error prior to raising the exception.
#       b. Debug-level logs which display interim steps of calculations and return values for the Loan functions.
#       c. Info-level logs to display things like ‘t is greater than term’ in the loan functions.
#       d. At the point the exception is caught (in your main function) use logging.exception to display
#           the exception in addition to a custom message.
#       e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to
#           take a long time, so the explicit versions are recommended).

# Importing necessary packages
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
from loan.mortgage import MortgageMixin, FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
from utils.timer import Timer

import logging
#######################
logging.basicConfig(format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style="{")
#######################


def main():
    logging.getLogger().setLevel(logging.INFO)  # Set logging level

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the __init__ function of Loan in the base loan class.
    #       2. Test the __init__ function of MortgageMixin
    #       3. Test the PMI() function of MortgageMixin with LTV based on asset value instead of loan's notional value
    #       4. Test the __init__ function of AutoLoan
    #       5. Test the recoveryValue function of Loan
    #       6. Test the equity function of Loan, showcase the logging 't is greater than term)
    #       7. Test the __init__ function of Loan
    #       8. Test the __init__ function of Loan
    #       9. Test the recursive function interestDueRecursive to showcase the recursive function warning logging
    #           and Timer logging
    #
    ###############################################
    # Test 1.1
    # Scenario: Test the __init__ function of Loan in the base loan class.
    #   The __init__ method will only works if the asset parameters is from the Asset family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    logging.info('Test 1.1')
    asset1 = Asset(1000000)
    car1 = Car(100000)
    loan1 = Loan(100000, .05, 30, asset1)
    loan1 = Loan(100000, .05, 30, car1)

    # Test 1.2
    # Scenario: Test the __init__ function of MortgageMixin
    #   The __init__ method will only works if the home parameters is from the HouseBase family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    logging.info('Test 1.2')
    car1 = Car(1000000)
    car2 = Lambourghini(1000000)
    housebase1 = HouseBase(1000000)
    primaryhome1 = PrimaryHome(100000)
    vacayhome1 = VacationHome(100000)
    mortgage1 = FixedMortgage(100000, .05, 30, housebase1)
    mortgage1 = FixedMortgage(100000, .05, 30, primaryhome1)
    mortgage1 = FixedMortgage(100000, .05, 30, vacayhome1)

    # Exception Handling block on intentionally incorrect passed-in value.
    # here: an incorrect type is passed into home
    try:
        mortgage1 = FixedMortgage(100000, .05, 30, car1)
    except ValueError as valEx:  # handle the asset type value error
        logging.getLogger().setLevel(logging.ERROR)
        logging.error(valEx)
        pass
    except Exception as Ex:  # catch other unknown error
        logging.exception(Ex)
        pass

    # Test 1.3
    # Scenario: 3. Test the PMI() function of MortgageMixin with LTV based on asset value
    #               instead of loan's notional value
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Test 1.3')
    logging.info(f'The PMI value is: {mortgage1.PMI(20000)}')

    # Test 1.4
    # Scenario: 4. Test the __init__ function of AutoLoan
    #   The __init__ method will only works if the car parameters is from the Car family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    logging.info('Test 1.4')
    autoloan1 = AutoLoan(100000, .05, 30, car1)
    autoloan2 = AutoLoan(100000, .05, 30, car2)

    # Exception Handling block on intentionally incorrect passed-in value.
    # here: an incorrect type is passed into car
    try:
        autoloan1 = AutoLoan(100000, .05, 30, vacayhome1)
    except ValueError as valEx:  # handle the asset type value error
        logging.getLogger().setLevel(logging.ERROR)
        logging.error(valEx)
        pass
    except Exception as Ex:  # catch other unknown error
        logging.exception(Ex)
        pass

    # Test 1.5
    # Scenario: 5. Test the recoveryValue function of Loan
    #   The recoveryValue method will return the current asset value for the given period
    #       times a recovery multiplier of .6
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Test 1.5')
    logging.info(f'The asset value for the given period is: {autoloan1.recoveryValue(20)}.')
    logging.info(f'The asset value for the given period is: {mortgage1.recoveryValue(20)}.')

    # Test 1.6
    # Scenario: 6. Test the equity function of Loan, showcase the logging 't is greater than term)
    #   The equity method will return the available equity (current asset value less current loan balance)
    logging.info('Test 1.6')
    logging.info(f'The current available equity is: {mortgage1.equity(100)}.')
    logging.info(f'The current available equity is: {autoloan2.equity(20)}.')

    # Test 1.7
    # Scenario: Test the __init__ function of Loan
    #   The __init__ method will only works if the asset parameters is from the Asset family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    # Exception Handling block on intentionally incorrect passed-in value.
    # here: a string is passed into asset
    logging.info('Test 1.7')
    try:
        loan1 = Loan(100000, .05, 30, 'sdfsf')
    except ValueError as valEx:  # handle the asset type value error
        logging.getLogger().setLevel(logging.ERROR)
        logging.error(valEx)
        pass
    except Exception as Ex:  # catch other unknown error
        logging.exception(Ex)
        pass


    # Test 1.8
    # Scenario: Test the __init__ function of Loan
    #   The __init__ method will only works if the asset parameters is from the Asset family (base or derived).
    #   Initialize the loan only if, else raise a value error.
    # Exception Handling block on intentionally incorrect passed-in value.
    # here: a tuple is passed into asset
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Test 1.8')
    try:
        loan1 = Loan(100000, .05, 30, (-1000, 'george'))
    except ValueError as valEx:  # handle the asset type value error
        logging.getLogger().setLevel(logging.ERROR)
        logging.error(valEx)
        pass
    except Exception as Ex:  # catch other unknown error
        logging.exception(Ex)
        pass

    # Test 1.9
    # Scenario: Test the recursive function interestDueRecursive to showcase the recursive function warning logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info('Test 1.9')

    loan1 = Loan(100000, .05, 30, asset1)

    # Time how long it takes recursive function to run
    # Input proper timer logging
    with Timer('interestDueRecursive'):
        try:   # Handle exceptions
            logging.info(f'Interest due of loan1 is {loan1.interestDueRecursive(2)}')  # Change term here
        except Exception:  # Catch unanticipated error
            logging.info(Exception('Unknown error.'))
            pass

    ###############################################


#######################
if __name__ == '__main__':
    main()
