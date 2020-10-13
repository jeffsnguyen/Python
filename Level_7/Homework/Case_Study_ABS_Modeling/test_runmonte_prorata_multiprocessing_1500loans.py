# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: Contains the code to test the ABS Model
# Test case: Test the ABS model with Monte Carlo on 1500 loans, on multiprocessing, prorata mode

#######################
# Importing necessary packages
import logging
from loan.loanpool import LoanPool
from utils.import_export import loansImportCSV, spvExportCSV
from spv.structured_securities import StructuredSecurities
from spv.waterfall import doWaterfall, simulateWaterfall, runMonte
import random
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

    # Test case: Test the ABS model with Monte Carlo on 1500 loans, on multiprocessing, prorata mode
    # Assets are from Loans.csv
    # Liabilities: originally start with these below tranches
    #   tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    #   tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    # Optimize tranches' rates based on a yield curve to get diff = 50 bps or less.
    # Print optimized rate on screen and run the Waterfall 1 time to get a CSV output of the transactions
    #   on 'liabilities_prorata_montecarlo_multiprocessing_1500loans.csv'
    ###############################################
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    random.seed(1)
    ###############################################
    loans1500 = LoanPool(loansImportCSV('Loans.csv'))
    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    tranches.setMode('Pro Rata')

    newTrancheRate = runMonte(loans1500, tranches, 0.1, 100, 20)
    print(f'My new tranche rate is = {newTrancheRate}')

    # Run the Waterfall once to generate CSV output of transactions.
    tranches = StructuredSecurities(loans1500.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', newTrancheRate[0], '1')
    tranches.addTranche('StandardTranche', '0.2', newTrancheRate[1], '2')
    tranches.setMode('Pro Rata')
    ledger, tranchesMetrics = simulateWaterfall(loans1500, tranches, 1)
    spvExportCSV(ledger, 'liabilities_prorata_montecarlo_multiprocessing_1500loans.csv')
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