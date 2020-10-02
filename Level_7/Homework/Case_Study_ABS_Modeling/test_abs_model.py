# Type: Homework
# Level: 6
# Section: 6.2: Concurrency
# Exercise: 1
# Description: Contains the code to simulate the Monte Hall problem, using multiprocessing
#   In this exercise, we will look to make the Monty Hall simulation achieve true multi-processing. This is
#       a good segue to financial Monte Carlo as the concepts and approaches are the same.
#
#   a) Create and initialize five processes. Note that starting processes takes some time, and is the
#       upfront cost of using multi-processing.
#   b) Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each).
#   c) Combine the five returned results lists and take the average, to get the overall result.
#   d) Time all of the above (starting from b). Does total runtime improve from the previous level?
#   e) Try decreasing/increasing the number of processes to determine the optimal runtime.
#
#   BONUS: Try the above using multithreading and compare/contrast the performance vs. multiprocessing.

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
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
    tranche1 = Tranche(100000, 0.05, 'B')
    standard_tranche1 = StandardTranche(tranche1)

    print(tranche1.__repr__())

    print()
    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
