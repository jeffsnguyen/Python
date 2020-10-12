# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the base Tranche class
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging
import numpy_financial

#######################

#######################


# Tranche Base class
class Tranche(object):
    def __init__(self, notional, rate, subordinationFlag):
        self._notional = notional
        self._rate = rate
        self._subordinationFlag = subordinationFlag
        self._r = 0  # Record IRR
        self._dirr = 0  # Record DIRR
        self._dirrLetter = None  # Record DIRR in letter form
        self._al = 0  # Record Average Life

    def __repr__(self):
        return f'{self.__class__.__name__}({self.notional}, {self.rate}, {self.subordinationFlag})'

    ##########################################################
    # Decorators to define and set values for instance variables

    # Decorator to create a property function to define the attribute notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set notional value
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the attribute rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set rate value
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute subordinationFlag
    @property
    def subordinationFlag(self):
        return self._subordinationFlag

    # Decorator to set subordinationFlag value
    @subordinationFlag.setter
    def subordinationFlag(self, isubordinationFlag):
        self._subordinationFlag = isubordinationFlag  # Set instance variable subordinationFlag from input

    # Decorator to create a property function to define the attribute r (IRR)
    @property
    def r(self):
        return self._r

    # Decorator to set r (IRR) value
    @r.setter
    def r(self, ir):
        self._r = ir  # Set instance variable r (IRR) from input

    # Decorator to create a property function to define the attribute dirr
    @property
    def dirr(self):
        return self._dirr

    # Decorator to set dirr value
    @dirr.setter
    def dirr(self, idirr):
        self._dirr = idirr  # Set instance variable dirr from input

    # Decorator to create a property function to define the attribute dirrLetter
    @property
    def dirrLetter(self):
        return self._dirrLetter

    # Decorator to set dirrLetter value
    @dirrLetter.setter
    def dirrLetter(self, idirrLetter):
        self._dirrLetter = idirrLetter  # Set instance variable dirrLetter from input

    # Decorator to create a property function to define the attribute al
    @property
    def al(self):
        return self._al

    # Decorator to set al value
    @al.setter
    def al(self, ial):
        self._al = ial  # Set instance variable al from input
    ##########################################################
    # Add instance methods

    # Return total payment made for each period t
    def paymentPerPeriod(self, t):
        raise NotImplementedError('Must override StandardTranche')

    # Return total payment period:
    def totalPaymentPeriod(self):
        raise NotImplementedError('Must override StandardTranche')

    # Calculate Internal Rate of Return (IRR)
    # This is the interest rate that results in the present value of all (monthly)
    #   cash flows being equal to the initial investment amount. The equation for this is as follows (where C is
    #   the payment at time t, T is the total number of periods, and r is the monthly rate):
    #       0 = -C_0 + \sum_{t=1}^{T} \frac{C_t}{(1+r)^t}
    def IRR(self):
        period = self.totalPaymentPeriod()  # Override method from StandardTranche
        cf = [-self.notional]  # Init cash flow array with notional cash outflow
        for t in range(1, period):
            cf.append(self.paymentPerPeriod(t))  # Override method from StandardTranche to find CF per period
        self.r = numpy_financial.irr(cf) * 12  # Return annualized IRR
        return self.r

    # Calculate Reduction in Yield (DIRR)
    # This is the tranche rate less the annual IRR. Essentially, the annual tranche
    #   rate is the annualized rate of return that the investor expects to earn whereas the IRR is the realized
    #   return. DIRR specifies how much the investor lost out on (hence, its maximum is 100% + the tranche
    #   rate). Additionally, DIRR is used to give a letter rating to the security.
    def DIRR(self):
        self.dirr = self.rate - self.IRR()
        return self.dirr

    # Get DIRR in letter form
    def DIRRLetter(self):
        self.dirrLetter = self.getRating(self.dirr)
        return self.dirrLetter

    # Calculate Average Life (AL)
    # The AL of the security is the average time that each dollar of its unpaid principal remains unpaid.
    # This is the inner product of the time period numbers (0, 1, 2, 3, etc.) and the principal payments,
    #   divided by the initial principal. For example, if you have the principal payment list as follows: [10000,
    #   90000, 35000, 0], the AL would be (0*0 + 1*10000 + 2*90000+2*35000+3*35000+4*0)/100000. If the
    #   loan was not paid down (balance != 0), then AL is infinite – in this case, return None.
    def AL(self):
        raise NotImplementedError('Must override StandardTranche')

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    # Look up rating based on DIRR
    # Method: sort the dict, then get the smallest value at which value >= DIIR. Lookup key from the inverted dict.
    @staticmethod
    def getRating(dirr):
        dirr = dirr / 100
        ratings = {'Aaa': 0.06,
                   'Aa1': 0.67,
                   'Aa2': 1.3,
                   'Aa3': 2.7,
                   'A1': 5.2,
                   'A2': 8.9,
                   'A3': 13,
                   'Baa1': 19,
                   'Baa2': 27,
                   'Baa3': 46,
                   'Ba1': 72,
                   'Ba2': 106,
                   'Ba3': 143,
                   'B1': 183,
                   'B2': 231,
                   'B3': 311,
                   'Caa': 2500,
                   'Ca': 10000}
        sorted_key = dict(sorted(ratings.items(), key=lambda k: k[1], reverse=False))  # Sort dict
        closest_value = min(sorted_key.values(), key=lambda v: v >= dirr)  # Smallest value at which v>= dict
        ratingsInv = {v: k for k, v in ratings.items()}  # Get the inverted dict to lookup key
        return ratingsInv[closest_value]
    ##########################################################
