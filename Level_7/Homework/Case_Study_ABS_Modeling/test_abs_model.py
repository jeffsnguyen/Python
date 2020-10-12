# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: Contains the code to test the ABS Model

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
from loan.loanpool import LoanPool
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
from loan.mortgage import FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from utils.import_export import loansImportCSV, spvExportCSV
from asset.asset import Car
from spv.structured_securities import StructuredSecurities
from spv.waterfall import doWaterfall, simulateWaterfall, runMonte
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='w', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


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
    ledger, tranchesMetrics = simulateWaterfall(loans, tranches, 1)
    spvExportCSV(ledger, 'liabilities_sequential_2loans.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter}\n'
              f' AL = {tranche.al}')
    print()
    print(f'Pro Rata mode:')
    tranches.setMode('Pro Rata')
    ledger, tranchesMetrics = simulateWaterfall(loans, tranches, 1)
    spvExportCSV(ledger, 'liabilities_prorata_2loans.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter}\n'
              f' AL = {tranche.al}')
    ###############################################

    # Re-init StructuredSecurities to take on bigger loan pool
    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.005', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.008', '2')
    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual large sample run of the Waterfall, sequential mode')
    tranches.setMode('Sequential')
    ledger, tranchesMetrics = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_sequential_1500loans.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter}\n'
              f' AL = {tranche.al}')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Manual large sample run of the Waterfall, pro rata mode')
    tranches.setMode('Pro Rata')
    ledger, tranchesMetrics = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_prorata_1500loans.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter}\n'
              f' AL = {tranche.al}')
    # Answer: Each tranches did get successfully paid down to 0 and there is money left at the end.
    ###############################################

    ###############################################
    print()
    testNum += 1
    print(f'Test {testNum}: Large sample run of Monte Carlo to converge yield on Sequential mode')

    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    tranches.setMode('Sequential')

    newTrancheRate = runMonte(loans1500, tranches, 0.005, 2000, 20)
    print(f'My new tranche rate is = {newTrancheRate}')
    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', newTrancheRate[0], '1')
    tranches.addTranche('StandardTranche', '0.2', newTrancheRate[1], '2')
    tranches.setMode('Sequential')
    ledger, tranchesMetrics = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_sequential_montecarlo_1500loans.csv')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter}\n'
              f' AL = {tranche.al}')

    ###############################################
###############################################


#######################
if __name__ == '__main__':
    main()