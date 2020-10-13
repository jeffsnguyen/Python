# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: Contains the code to test the ABS Model
# Test the ABS model with a single process and 2 loans on sequential mode

#######################
# Importing necessary packages
import logging
from loan.loanpool import LoanPool
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
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

    # Test case: Test the ABS model with a single process and 2 loans on sequential mode
    # Assets are:
    #   AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    #   AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    # Liabilities:
    #   tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    #   tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    # Run the Waterfall 1 time to get a CSV output of the transactions
    #   on 'liabilities_sequential_2loans.csv'
    ###############################################
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])
    tranches = StructuredSecurities(loans.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    tranches.setMode('Sequential')

    ledger, tranchesMetrics = simulateWaterfall(loans, tranches, 1)
    spvExportCSV(ledger, 'liabilities_sequential_2loans.csv')
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

