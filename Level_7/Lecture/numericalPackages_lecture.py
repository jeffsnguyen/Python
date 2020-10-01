# numerical packages  lecture

import numpy


def main():
    # Similar to base package but can specify how many numbers to generate by 3rd parameter
    # Output to a numpy array can be easily converted to a list
    arrayRandint = numpy.random.randint(1, 500, 100)
    print(arrayRandint)
    print(list(arrayRandint))
    print()

    # Non-integer
    arrayUniform = numpy.random.uniform(1, 500, 100)
    print(arrayUniform)
    print()

    # Internal Rate of Return
    l = [100, 150, 200, 250]  # List of CF
    p = -175  # Initial CF out to buy teh bond
    r = numpy.irr([-175, 100, 150, 200, 250])
    print(r)

    r = numpy.irr([p] + l)
    print(r)
    print()


#######################
if __name__ == '__main__':
    main()
