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
from spv.waterfall import doWaterfall, simulateWaterfall
from math import e, sqrt
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


def calculateYield(dirrAvg, alAvg):
    return ((7 / (1 + 0.08 * e**(-0.19 * alAvg / 12))) + (0.019 * sqrt((alAvg / 12) * dirrAvg * 100))) / 100

def runMonte(loans, tranches, tolerance, nsim):
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')

    while True:
        ledger, reserve, r, dirrAvg, dirrLetter, alAvg = simulateWaterfall(loans, tranches, nsim)
        yieldVal = calculateYield(dirrAvg, alAvg)

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
    logging.getLogger().setLevel(logging.ERROR)
    testNum = 0

    # Init test loans variables
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])
    loans1500 = LoanPool(loansImportCSV('Loans.csv'))

    tranches = StructuredSecurities(loans.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual small sample run of the Waterfall on Sequential mode')

    print(f'Sequential mode:')
    tranches.setMode('Sequential')
    ledger, reserve, r, dirr, dirrLetter, al = simulateWaterfall(loans, tranches, 1)
    print(f'My ledger is:\n{ledger}')
    print(f'My reserve account is:\n{reserve}')
    for tranche in tranches.tranches:
        print(f'{tranche}\nIRR = {r}\nDIRR = {dirrLetter}\nAL = {al}')
    print()
    print(f'Pro Rata mode:')
    tranches.setMode('Pro Rata')
    ledger, reserve, r, dirr, dirrLetter, al = simulateWaterfall(loans, tranches, 1)
    print(f'My ledger is:\n{ledger}')
    print(f'My reserve account is:\n{reserve}')
    for tranche in tranches.tranches:
        print(f'{tranche}\nIRR = {r}\nDIRR = {dirrLetter}\nAL = {al}')
    ###############################################

    # Re-init StructuredSecurities to take on bigger loan pool
    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual large sample run of the Waterfall, sequential mode')
    tranches.setMode('Sequential')
    ledger, reserve, r, dirr, dirrLetter, al = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_sequential.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\nIRR = {r}\nDIRR = {dirrLetter}\nAL = {al}')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual large sample run of the Waterfall, pro rata mode')
    tranches.setMode('Pro Rata')
    ledger, reserve, r, dirr, dirrLetter, al = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_prorata.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\nIRR = {r}\nDIRR = {dirrLetter}\nAL = {al}')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
