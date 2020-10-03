# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the base Tranche class
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging
from spv.tranche_base import Tranche
from utils.run_once import run_once
#######################

#######################



# Standard Tranche class
# Standard tranches receive both interest and principal payments from the pool of loans.
class StandardTranche(Tranche):
    def __init__(self, notional, rate, timePeriod, subordinationFlag):
        # Invoke base class init
        super(StandardTranche, self).__init__(notional, rate, timePeriod, subordinationFlag)
        self._timePeriod = timePeriod

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car

    ##########################################################
    # Add instance methods

    # Increase the current time period of the object
    def increaseTimePeriod(self):
        self._timePeriod += 1
        return self._timePeriod

    # Record principal payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    @run_once
    def makePrincipalPayment(self, timeperiod):
        pass

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
