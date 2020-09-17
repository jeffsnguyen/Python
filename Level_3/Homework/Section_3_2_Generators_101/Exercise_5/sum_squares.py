# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 5
# Description: Contains the tests of speed comparison between generators and list comprehension
#   Generator expressions:
#       a. Create a list comprehension that contains the square of all numbers from 0-5,000,000, using
#           range. Sum this using the built-in sum function.
#       b. Compare the total time taken to build and sum each. Which one is faster? What are the
#           benefits of using the generator instead of the list comprehension? Why?

#######################
# Importing necessary packages
from utils.timer import Timer

#######################

###############################################


###############################################
def main():


    # Testing block 1
    # Scenario:
    #   This block will:
    #       1.1 Test the time it takes to do sum of squares of all numbers [0, 500000] using list comprehension
    #       1.2 Test the time it takes to do sum of squares of all numbers [0, 500000] using generators

    ###############################################

    # Test 1.1
    # 1.1 Test the time it takes to do sum of squares of all numbers [0, 500000] using list comprehension
    print('Test 1 Test the time it takes to do sum of squares of all numbers [0, 500000] using list comprehension')
    t = Timer()
    t.start()
    # List comprehension to sum all numbers from 0 - 500000
    sum_listcomp = sum([i**2 for i in range(0, 500000)])
    t.end()
    print('The sum of squares is:', sum_listcomp)
    print()

    # Test 1.2
    # 1.2 Test the time it takes to do sum of squares of all numbers [0, 500000] using generators
    print('1.2 Test the time it takes to do sum of squares of all numbers [0, 500000] using generators')
    t = Timer()
    t.start()
    # Generator to sum all numbers from 0 - 500000
    sum_generator = sum(i ** 2 for i in range(0, 500000))
    t.end()
    print('The sum of squares is:', sum_generator)

    # With range 0 - 500,000, list comprehension takes less time vs. generators.
    # However when range increase 0 - 5,000,000, generators are faster.
    # Generators are faster with large number of computations as generators are only evaluated on an as needed basis
    #   thus, saves memory and be more efficient/faster.

###############################################

#######################
if __name__ == '__main__':
    main()