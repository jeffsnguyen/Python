# loan base class 2.2.3 lecture


class Loan(object):
    def __init__(self, asset, face, rate, term):
        self._asset = asset
        self._face = face
        self._rate = rate
        self._term = term

    # Add getter/setter property functions

    def rate(self, period):
        # Should be overridden by derived class
        raise NotImplementedError

    def monthlyPmt(self):
        pass

    def balance(self):
        pass


    # Other loan functions




