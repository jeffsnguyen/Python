# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 8
# Description: Create three generator expressions and use the appropriate itertools function to get all the
#   combinations of the values. Print out the result as a list.

#######################
# Importing necessary packages
from itertools import combinations, chain
#######################

###############################################


###############################################
def main():

    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test combinations using generator expression

    ###############################################

    # Test 1
    # 1. Test combinations using generator expression

    print('Test 1: Test combinations using generator expression')

    # Generator to display some text multiple times
    gen1 = ('Pandemic' for i in range(3))
    gen2 = ('P' for i in range(3))
    gen3 = ('13' for i in range(3))

    gen = combinations(chain(gen1, gen2, gen3), 3)  # use combinations after chaining to obtain combos
    print(list(gen))  # printout as a list

###############################################

#######################
if __name__ == '__main__':
    main()