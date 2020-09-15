# callable lectures



def main():
    # lambda
    square = lambda n: n**2
    print(square(2))

    # Filter
    loanAmounts = [100000, 150000, 500000, 1000000]
    print(list(filter(lambda val:val >100000, loanAmounts)))

    # map
    # use to transform a list
    rates = [.04, .0375, .032, .054]
    # first zip 2 lists then face_rate[0] correspond to 1st list, which is loanAmounts
    print(list(map(lambda face_rate: face_rate[0]*face_rate[1], zip(loanAmounts, rates))))

    # reduce
    # allows to accumulate a value recursively
    from functools import reduce

    # zip the list, start from the amount in the 3rd parameters, total = 00 in this case
    #
    reduce(lambda total, face_rate: total + (face_rate[0]*face_rate[1]), zip(loanAmounts, rates), 0)


#######################
if __name__ == '__main__':
    main()