# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the base Tranche class
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging

#######################

#######################


# Tranche Base class
class Tranche(object):
    def __init__(self, notional, rate, subordinationFlag):
        self._notional = notional
        self._rate = rate
        self._subordinationFlag = subordinationFlag

    def __repr__(self):
        return f'{self.__class__.__name__}({self._notional}, {self._rate}, {self._subordinationFlag})'
