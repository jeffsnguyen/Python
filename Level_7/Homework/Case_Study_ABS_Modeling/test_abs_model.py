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
from asset.asset import Car
from spv.structured_securities import StructuredSecurities
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

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    dT_start1 = '2018-08-21 12:5:30:123456'
    dT_start1 = datetime.datetime.strptime(dT_start1, '%Y-%m-%d %H:%M:%S:%f')
    dT_end1 = dT_start1 + datetime.timedelta(days=300)

    dT_start2 = '2018-08-21 12:5:30:123456'
    dT_start2 = datetime.datetime.strptime(dT_start2, '%Y-%m-%d %H:%M:%S:%f')
    dT_end2 = dT_start2 + datetime.timedelta(days=240)

    rate1 = 0.08
    rate2 = 0.06

    loan1 = AutoLoan(notional=100000, rate=rate1, maturity_start=dT_start1, maturity_end=dT_end1, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=rate2, maturity_start=dT_start2, maturity_end=dT_end2, car=Car(75000))
    loans = LoanPool([loan1, loan2])

    sum_principal = loans.totalPrincipal()
    print(f'Term of {loan1.__repr__()} = {loan1.term()} months')
    print(f'Term of {loan2.__repr__()} = {loan2.term()} months')
    print()

    print(f'Monthly payment of {loan1.__repr__()} at t=0 = {loan1.monthlyPayment(0)}')
    print(f'Monthly payment of {loan2.__repr__()} at t=0 = {loan2.monthlyPayment(0)}')
    print(f'Monthly payment of {loan1.__repr__()} at t=10 = {loan1.monthlyPayment(10)}')
    print(f'Monthly payment of {loan2.__repr__()} at t=8 = {loan2.monthlyPayment(8)}')
    print(f'Monthly payment of {loan1.__repr__()} at t=11 = {loan1.monthlyPayment(11)}')
    print(f'Monthly payment of {loan2.__repr__()} at t=9 = {loan2.monthlyPayment(9)}')
    print()

    print(f'Interest due of {loan1.__repr__()} at t=0 = {loan1.interestDue(0)}')
    print(f'Interest due of {loan2.__repr__()} at t=0 = {loan2.interestDue(0)}')
    print(f'Interest due of {loan1.__repr__()} at t=1 = {loan1.interestDue(1)}')
    print(f'Interest due of {loan2.__repr__()} at t=1 = {loan2.interestDue(1)}')
    print(f'Interest due of {loan1.__repr__()} at t=10 = {loan1.interestDue(10)}')
    print(f'Interest due of {loan2.__repr__()} at t=8 = {loan2.interestDue(8)}')
    print(f'Interest due of {loan1.__repr__()} at t=11 = {loan1.interestDue(11)}')
    print(f'Interest due of {loan2.__repr__()} at t=9 = {loan2.interestDue(9)}')
    print()

    print(f'Principal due of {loan1.__repr__()} at t=0 = {loan1.principalDue(0)}')
    print(f'Principal due of {loan2.__repr__()} at t=0 = {loan2.principalDue(0)}')
    print(f'Principal due of {loan1.__repr__()} at t=1 = {loan1.principalDue(1)}')
    print(f'Principal due of {loan2.__repr__()} at t=1 = {loan2.principalDue(1)}')
    print(f'Principal due of {loan1.__repr__()} at t=10 = {loan1.principalDue(10)}')
    print(f'Principal due of {loan2.__repr__()} at t=8 = {loan2.principalDue(8)}')
    print(f'Principal due of {loan1.__repr__()} at t=11 = {loan1.principalDue(11)}')
    print(f'Principal due of {loan2.__repr__()} at t=9 = {loan2.principalDue(9)}')
    print()

    print(f'Total Payments of {loan1.__repr__()} = {loan1.totalPayments()}')
    print(f'Total Payments of {loan2.__repr__()} = {loan2.totalPayments()}')
    print()

    print(f'Total Interests of {loan1.__repr__()} = {loan1.totalInterest()}')
    print(f'Total Interests of {loan2.__repr__()} = {loan2.totalInterest()}')
    print()

    print(f'Balance of {loan1.__repr__()} at t=0 = {loan1.balance(0)}')
    print(f'Balance of {loan2.__repr__()} at t=0 = {loan2.balance(0)}')
    print(f'Balance of {loan1.__repr__()} at t=1 = {loan1.balance(1)}')
    print(f'Balance of {loan2.__repr__()} at t=1 = {loan2.balance(1)}')
    print(f'Balance of {loan1.__repr__()} at t=9 = {loan1.balance(9)}')
    print(f'Balance of {loan2.__repr__()} at t=7 = {loan2.balance(7)}')
    print(f'Balance of {loan1.__repr__()} at t=10 = {loan1.balance(10)}')
    print(f'Balance of {loan2.__repr__()} at t=8 = {loan2.balance(8)}')
    print()

    print(f'Active loans at time t=0 = {loans.activeLoanCount(0)}')
    print(f'Active loans at time t=8 = {loans.activeLoanCount(8)}')
    print(f'Active loans at time t=9 = {loans.activeLoanCount(9)}')
    print(f'Active loans at time t=11 = {loans.activeLoanCount(11)}')
    print()

    print(f'Total payment at time t=0 = {loans.totalPayments(0)}')
    print(f'Total payment at time t=7 = {loans.totalPayments(7)}')
    print(f'Total payment at time t=9 = {loans.totalPayments(9)}')
    print(f'Total payment at time t=10 = {loans.totalPayments(10)}')
    print()

    print(f'Total principal = {loans.totalPrincipal()}')
    print()

    print(f'Payment due at time t=0 = {loans.paymentDue(0)}')
    print(f'Payment due at time t=7 = {loans.paymentDue(7)}')
    print(f'Payment due at time t=8 = {loans.paymentDue(8)}')
    print(f'Payment due at time t=11 = {loans.paymentDue(11)}')
    print()

    print(f'Total Interest at time t=0 = {loans.totalInterest(0)}')
    print(f'Total Interest at time t=1 = {loans.totalInterest(1)}')
    print(f'Total Interest at time t=8 = {loans.totalInterest(8)}')
    print(f'Total Interest at time t=11 = {loans.totalInterest(11)}')
    print()

    print(f'Principal due at time t=0 = {loans.principalDue(0)}')
    print(f'Principal due at time t=1 = {loans.principalDue(1)}')
    print(f'Principal due at time t=9 = {loans.principalDue(9)}')
    print(f'Principal due at time t=11 = {loans.principalDue(11)}')
    print()

    print(f'{loans.totalPayments(9)}')
    print()

    wA = 0.8
    wB = 0.2
    rateA = 0.05
    rateB = 0.08
    notionalA = sum_principal * wA
    notionalB = sum_principal * wB

    trancheA = StandardTranche(notionalA, rateA, 1)
    trancheB = StandardTranche(notionalB, rateB, 2)

    print(trancheA.__repr__())
    print(trancheB.__repr__())

    print(f'Tranche A notional amount = {trancheA._notional}')
    print(f'Tranche B notional amount = {trancheB._notional}')
    print()

    #trancheA.makePrincipalPayment(1, 18915.8191)
    #print(f'Tranche A principaid = {trancheA._principalPaid}')
    print()

    print(f'Tranche A notional Balance at t=0 = {trancheA.notionalBalance(0)}')
    print(f'Tranche A notional Balance at t=1 = {trancheA.notionalBalance(1)}')
    print()

    print(f'Tranche A interest due of period t=0 = {trancheA.interestDue(0)}')
    print(f'Tranche A interest shortfall of period t=0 = {trancheA._interestShortFall[0]}')
    print(f'Tranche A interest due of period t=1 = {trancheA.interestDue(1)}')
    #trancheA.makeInterestPayment(1, trancheA.interestDue(1))
    print(trancheA._principalPaid)

    #print(f'Tranche A interest shortfall of period t=1 = {trancheA._interestShortFall[1]}')
    # print(f'Tranche A interest due of period t=2 = {trancheA.interestDue(2)}')
    print()

    # Instantiate StructuredSecurities
    tranches = [trancheB, trancheA]
    structuredSecurities1 = StructuredSecurities(tranches)
    print(f'{structuredSecurities1.__repr__()}')
    print(f'{type(structuredSecurities1)}')
    print(f'{structuredSecurities1._tranches}')
    print(f'{type(structuredSecurities1._tranches)}')
    print(f'{sum(tranche._notional for tranche in structuredSecurities1._tranches)}')
    print()

    # Test addTranche()
    #structuredSecurities1.addTranche('StandardTranche', 0.2, .02, 2)
    #print(f'{structuredSecurities1._tranches}')
    #print()
    sumcollections = 0
    # Test makeInterestPayments() t
    for i in range(1,11):
        logging.debug(f'The current recorded period is {structuredSecurities1._timePeriod}')
        print(f'Payment due of the collection at t={i} = {loans.paymentDue(i)}')
        print(f'Principal received from the collection at t={i} = {loans.principalDue(i)}')
        collections = loans.paymentDue(i)
        sumcollections += collections
        principalCollected = loans.principalDue(i)
        structuredSecurities1.get_principalCollected(i, principalCollected)
        logging.debug(f'Main shows my CF to be used at t={i} is {collections}')
        availableFunds = structuredSecurities1.makeInterestPayments(collections)
        print(f'TrancheA interest due at t={i} = {trancheA._interestDue[i]}')
        print(f'TrancheA interest paid at t={i} = {trancheA._interestPaid[i]}')
        print(f'TrancheA interest short fall at t={i} = {trancheA._interestShortFall[i]}')
        print(f'TrancheB interest due at t={i} = {trancheB._interestDue[i]}')
        print(f'TrancheB interest paid at t={i} = {trancheB._interestPaid[i]}')
        print(f'TrancheB interest short fall at t={i} = {trancheB._interestShortFall[i]}')
        print(f'Available Funds after paying interest t={i} = {availableFunds}')
        # Test makeSeqPrinPayments()
        availableFunds = structuredSecurities1.makeSeqPrinPayments(availableFunds)
        print(f'TrancheA principal due at t={i} = {trancheA._principalDue[i]}')
        print(f'TrancheA principal paid at t={i} = {trancheA._principalPaid[i]}')
        print(f'TrancheA principal short fall at t={i} = {trancheA._principalShortFall[i]}')
        print(f'TrancheB principal due at t={i} = {trancheB._principalDue[i]}')
        print(f'TrancheB principal paid at t={i} = {trancheB._principalPaid[i]}')
        print(f'TrancheB principal short fall at t={i} = {trancheB._principalShortFall[i]}')
        print(f'Available Funds after paying principal t={i} = {availableFunds}')
        structuredSecurities1.increaseTranchesTimePeriod()
        logging.debug(f'################################################################')
        print()


    print(f'TrancheA principal paid = {trancheA._principalPaid}')
    print(f'TrancheA principal short fall = {trancheA._principalShortFall}')
    print(f'TrancheA principal due = {trancheA._principalDue}')
    print(f'TrancheA interest paid = {trancheA._interestPaid}')
    print(f'TrancheA interest short fall = {trancheA._interestShortFall}')
    print(f'TrancheA interest due = {trancheA._interestDue}')
    print()
    print(f'TrancheB principal paid = {trancheB._principalPaid}')
    print(f'TrancheB principal short fall = {trancheB._principalShortFall}')
    print(f'TrancheB principal due = {trancheB._principalDue}')
    print(f'TrancheB interest paid = {trancheB._interestPaid}')
    print(f'TrancheB interest short fall = {trancheB._interestShortFall}')
    print(f'TrancheB interest due = {trancheB._interestDue}')
    print(f'SS cash reserve is {structuredSecurities1._reserve}')
    print()

    print(f'TrancheA total interest paid = {sum(trancheA._interestPaid.values())}')
    print(f'TrancheB total interest paid = {sum(trancheB._interestPaid.values())}')
    print(f'TrancheA total principal paid = {sum(trancheA._principalPaid.values())}')
    print(f'TrancheB total principal paid = {sum(trancheB._principalPaid.values())}')
    print(f'SS total collections: {sumcollections}')
    '''
    # Test increaseTrancheTimePeriod()
    print(structuredSecurities1._tranches[0]._timePeriod)
    print(structuredSecurities1._tranches[1]._timePeriod)
    #print(structuredSecurities1._tranches[2]._timePeriod)
    structuredSecurities1.increaseTrancheTimePeriod()
    print(structuredSecurities1._tranches[0]._timePeriod)
    print(structuredSecurities1._tranches[1]._timePeriod)
    #print(structuredSecurities1._tranches[2]._timePeriod)
    print()
    '''


    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
