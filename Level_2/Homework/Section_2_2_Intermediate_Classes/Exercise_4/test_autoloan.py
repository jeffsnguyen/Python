# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 4
# Description: This contains test for AutoLoan class methods.
#   Create a fixed AutoLoan class. This should derive-from the appropriate base class(es).

# Importing necessary packages
from loan.loans import AutoLoan, FixedRateLoan
#######################


def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the init function of AutoLoan
    #       2. Test the rate() method via FixedRateLoan
    ###############################################
    # 1. Testing AutoLoan class
    # Scenario: Assign an AutoLoan class variable
    # Desire result: Print correct result as assigned
    autoloan1 = AutoLoan(100000, .050, 30, 100000)
    print('Test block 1: AutoLoan')
    print('Test 1.1')
    print('The auto loan term is: ', autoloan1.__repr__())
    print('The auto loan rate is: ', autoloan1.rate())
    print()

    ###############################################
#######################
if __name__ == '__main__':
    main()
