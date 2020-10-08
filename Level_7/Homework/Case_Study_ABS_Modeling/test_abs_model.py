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
from utils.import_export import loansImportCSV, spvExportCSV
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


# Initialize StructuredSecurities tranches
def tranchesInit(loans):
    tranches = StructuredSecurities(loans.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    return tranches


# Run the sequential mode Waterfall one time
def runSequentialSim(loans):
    tranches = tranchesInit(loans)
    tranches.setMode('Sequential')
    return doWaterfall(loans, tranches)


# Run the Pro Rata mode Waterfall one time
def runProRataSim(loans):
    tranches = tranchesInit(loans)
    tranches.setMode('Pro Rata')
    return doWaterfall(loans, tranches)

###############################################
def main():

    # Test cases:
    #   1. Manual small sample run of the Waterfall
    #       i. on Sequential mode
    #       ii. on Pro Rata mode
    #   2. Test the Waterfall using loan data from 'Loans.csv' in sequential mode
    #       i. Instantiate the Loans object from the CSV
    #       ii. Instantiate the StructuredSecurity object
    #       iii. Run doWaterfall and export result to 'liabilities_sequential.csv
    #   3. Do 2. in Pro Rata mode, exporting to 'liabilities_prorata.csv'
    ###############################################
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)
    testNum = 0

    # Init test variables
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])
    loans1500 = LoanPool(loansImportCSV('Loans.csv'))
    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual small sample run of the Waterfall on Sequential mode')

    print(f'Sequential mode:')
    ledger, reserve = runSequentialSim(loans)
    print(f'My ledger is:\n{ledger}')
    print(f'My reserve account is:\n{reserve}')
    print()
    print(f'Pro Rata mode:')
    ledger, reserve = runProRataSim(loans)
    print(f'My ledger is:\n{ledger}')
    print(f'My reserve account is:\n{reserve}')
    ###############################################

    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual small sample run of the Waterfall, sequential mode')
    tranchesLedger, tranchesReserve = runSequentialSim(loans1500)
    spvExportCSV(tranchesLedger, 'liabilities_sequential.csv')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual small sample run of the Waterfall, pro rata mode')
    tranchesLedger2, tranchesReserve2 = runProRataSim(loans1500)
    spvExportCSV(tranchesLedger2, 'liabilities_prorata.csv')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
