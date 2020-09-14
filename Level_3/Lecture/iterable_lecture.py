# iterable functions lectures


import itertools
import operator

def main():
    # list is an iterable with __iter__ function
    yieldCurve = [.035, .025, .045, .065]

    # get iterator object
    yi = iter(yieldCurve)

    # first value from iterator
    print(next(yi))

    # chain allows connection of iterator
    rates = iter([.02, .03])
    ratesContinued = iter([.04, .05])
    allRates = itertools.chain(rates, ratesContinued)
    for rate in allRates:
        print(rate)

    # enumerate gives enumeration of each value in an iterable
    for i, rate in enumerate(allRates):
        print(str(i) + ': ' + str(rate))

    # accumulate is similar to reduce but shows each steps
    l = [3, 4, 5, 6]
    print (list(itertools.accumulate(l)))
    #set an initial value
    l = [3, 4, 5, 6]
    #print(list(itertools.accumulate(l, initial=5)))

    # operator
    # accumulate is similar to reduce but shows each steps
    l = [3, 4, 5, 6]
    print(list(itertools.accumulate(l, func=operator.add)))
    print(list(itertools.accumulate(l, func = operator.mul)))

    # product
    l1 = [1, 2, 3]
    l2 = ['a', 'b', 'c']
    l3 = [7, 8, 9]
    print(list(itertools.product(l1, l2, l3)))

#######################
if __name__ == '__main__':
    main()