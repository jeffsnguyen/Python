# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 7
# Description: Contains the tests for zip
# Create three generator expressions and zip them together. Print out the result as a list.

#######################
# Importing necessary packages

#######################

###############################################


###############################################
def main():

    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test zip using generator expression

    ###############################################

    # Test 1
    # 1. Test zip using generator expression

    print('Test 1: Test zip using generator expression')

    # Generator to display some text multiple times
    gen1 = ('Pandemic' for i in range(3))
    gen2 = ('P' for i in range(3))
    gen3 = ('13' for i in range(3))

    gen = zip(gen1, gen2, gen3) # zip to zip them together
    print(list(gen)) # printout as a list

###############################################

#######################
if __name__ == '__main__':
    main()