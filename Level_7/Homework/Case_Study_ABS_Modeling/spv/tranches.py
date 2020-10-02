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
#######################

#######################


# Standard Tranche class
# Standard tranches receive both interest and principal payments from the pool of loans.
class StandardTranche(Tranche):
    def __init__(self, notional, rate, subordinationFlag):
        # Invoke base class init
        super(StandardTranche, self).__init__(notional, rate, subordinationFlag)

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car
    @property
    def car(self):
        return self._car

    # Decorator to set car value
    @car.setter
    def car(self, icar):
        self._car = icar  # Set instance variable car from input

    ##########################################################
    # Add instance methods

    # Increase the current time period of the object
    def increaseTimePeriod(self):
        pass

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
