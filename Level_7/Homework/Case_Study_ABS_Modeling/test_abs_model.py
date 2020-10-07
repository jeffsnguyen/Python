# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: Contains the code to test the ABS Model

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
import datetime
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
from loan.loanpool import LoanPool
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
from loan.mortgage import FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from loan.loanIO import loanReadCSV, importCSV
from asset.asset import Car
from spv.structured_securities import StructuredSecurities
from spv.waterfall import doWaterfall
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


###############################################
def main():

    # Test case:
    #   1. Manual small sample run of the Waterfall
    #   2. Test the Waterfall using loan data from 'Loans.csv'
    #       i. Instantiate the Loans object from the CSV
    #       ii. Instantiate the StructuredSecurity object
    #       iii. Run doWaterfall and save the result in the CSV file.
    ###############################################
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    print()
    testNum = 1
    print(f'Test {testNum}: Manual small sample run of the Waterfall')
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])

    structuredSecurities = StructuredSecurities(loans.totalPrincipal())
    structuredSecurities.addTranche('StandardTranche', '0.8', '0.05', '1')
    structuredSecurities.addTranche('StandardTranche', '0.2', '0.08', '2')

    doWaterfall(loans, structuredSecurities)
    ###############################################

    ###############################################
    print()
    testNum = 2
    print(f'Test {testNum}: Manual small sample run of the Waterfall')

    loans = LoanPool(importCSV('Loans.csv'))
    structuredSecurities = StructuredSecurities(loans.totalPrincipal())
    structuredSecurities.addTranche('StandardTranche', '0.8', '0.05', '1')
    structuredSecurities.addTranche('StandardTranche', '0.2', '0.08', '2')

    doWaterfall(loans, structuredSecurities)
    ###############################################
###############################################


#######################
if __name__ == '__main__':
    main()
