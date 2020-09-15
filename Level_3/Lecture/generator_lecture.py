#  generator functions lectures


def getRate():
    rateCurve = [.035, .025, .045, .065, .07]

    # get the next rate on that list, one rate a time
    # instead of return rateCurve which return the enture list
    for rate in rateCurve:
        yield rate # when use yield, the function becomes a generator

def evenIntegers():
    i = -1
    while True: # infinite loop
        i += 1
        if not i % 2:
            yield i

def main():
    allRates = getRate()
    print(next(allRates))
    print(next(allRates))

    i = evenIntegers()
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    # use generator similar to list comprehension but without a bracket
    print((i**4 for i in range(5)))

    a = 'p'
    print(int(p))

#######################
if __name__ == '__main__':
    main()