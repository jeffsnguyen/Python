# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the base StructuredSecurities class
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
#######################

#######################


# StructuredSecurities Base class
# Consists of Tranche objects (composition)
class StructuredSecurities(object):
    def __init__(self, tranches):
        self._tranches = tranches
        self._tranche = [tranche for tranche in tranches]
        self._notional = [tranche._notional for tranche in tranches]
        '''
        self._rate = [tranche._rate for tranche in tranches]
        self._term = [tranche._term for tranche in tranches]
        self._subordinationFlag = [tranche._subordinationFlag for tranche in tranches]
        '''
    def __repr__(self):
        return [f'{tranche.__class__.__name__}({tranche._notional}, {tranche._rate}, {tranche._subordinationFlag})'
                for tranche in self._tranches]

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car

    ##########################################################
    # Add instance methods

    # Factory method to add tranche to StructuredSecurity object
    # Assume all inputs are type 'str'
    def addTranche(self, nameClass, notionalPct, rate, subordinationLvl):
        try:  # Handle instantiation of tranche object
            trancheObject = eval(nameClass)((float(notionalPct) * sum(self._notional)), float(rate), subordinationLvl)
        except ValueError as valEx:
            logging.error(f'{valEx("Failed to add. Incorrect input.")}')
        else:
            self._tranches.append(trancheObject)  # Add new object to list of StructuredSecurities
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
