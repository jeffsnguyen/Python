# Type: Homework
# Level: 5
# Section: 5.1: Date/Time
# Exercise: 6
# Description: This contains tests for Loan classes
#   Modify your Loan classes to take a loan start date and loan end (maturity) date instead of a term
#       parameter. Create a term method that calculates and returns the loan term (in months) from the
#       two dates. Assume that a month is 30 days and that you round the fractional month to the nearest integer.

# Importing necessary packages
import logging
import datetime
from loan.loan_base import Loan
from asset.asset import Asset, Car
from loan.loans import AutoLoan
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################


def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the init and other methods of Loan with new datetime parameters
    #       2. Test the init and other methods of Loan derived class with new datetime parameters

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')
    print('1. Test the init and other methods of Loan with new datetime parameters')
    logging.info('1. Test the init and other methods of Loan with new datetime parameters')

    dT_start = '2018-08-21 12:5:30:123456'
    dT_start = datetime.datetime.strptime(dT_start, '%Y-%m-%d %H:%M:%S:%f')
    dT_end = '2048-09-23 1:6:30:123456'
    dT_end = datetime.datetime.strptime(dT_end, '%Y-%m-%d %H:%M:%S:%f')
    loan1 = Loan(100000, 0.05, dT_start, dT_end, Asset(100000))

    print(f'Loan = {loan1}')
    print(f'Loan class = {type(loan1)}')
    print(f'Loan asset class = {type(loan1.asset)}')
    print(f'Loan term = {loan1.term()}')
    print(f'Loan monthly payments = {loan1.monthlyPayment()}')
    print(f'loan total payments = {loan1.totalPayments()}')
    print(f'loan total interest = {loan1.totalInterest()}')
    print(f'loan interest due at month 12th = {loan1.interestDue(12)}')
    print(f'loan principal due at month 12th = {loan1.principalDue(12)}')
    print(f'loan balance at month 120th = {loan1.balance(120)}')
    print(f'loan rate = {loan1.getRate()}')
    print()

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 2
    testNum = 'Test 2'
    logging.info(f'{testNum}')
    print('2. Test the init and other methods of Loan derived class with new datetime parameters')
    logging.info('2. Test the init and other methods of Loan derived class with new datetime parameters')

    dT_start = '2018-08-21 12:5:30:123456'
    dT_start = datetime.datetime.strptime(dT_start, '%Y-%m-%d %H:%M:%S:%f')
    dT_end = '2048-09-23 1:6:30:123456'
    dT_end = datetime.datetime.strptime(dT_end, '%Y-%m-%d %H:%M:%S:%f')
    loan1 = AutoLoan(100000, 0.05, dT_start, dT_end, Car(100000))

    print(f'Loan = {loan1}')
    print(f'Loan class = {type(loan1)}')
    print(f'Loan asset class = {type(loan1.asset)}')
    print(f'Loan term = {loan1.term()}')
    print(f'Loan monthly payments = {loan1.monthlyPayment()}')
    print(f'loan total payments = {loan1.totalPayments()}')
    print(f'loan total interest = {loan1.totalInterest()}')
    print(f'loan interest due at month 12th = {loan1.interestDue(12)}')
    print(f'loan principal due at month 12th = {loan1.principalDue(12)}')
    print(f'loan balance at month 120th = {loan1.balance(120)}')
    print(f'loan rate = {loan1.getRate()}')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    ###############################################


#######################
if __name__ == '__main__':
    main()
