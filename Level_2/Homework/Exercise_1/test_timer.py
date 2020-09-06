## Type: Homework
## Level: 1
## Section: 2.1: Classes
## Exercise: 1
## Description: This contains the test function for the class Timer

# Importing necessary packages
from utils.timer import Timer


#######################
# Create a testing function to run a meaningless loop to take up some time
# so that the Timer class can be tested
def testing_loop(x):
    print('Running a meaningless count from 1 to ' + str(x) + ' to test the Timer class...')

    # Run the meaningless loop to test
    count = 0
    for i in range(1, x):
        count += i

    # Signal completion of loop
    print('Loop completed.')


#######################


def main():
    # Initialize t with Timer class
    t = Timer(12, 45, 476)

    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #####
    testing_loop(10000000)
    #####
    t.end()  # Stop counter and print result

    t.timerConfig(3600)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #####
    testing_loop(20000000)
    #####
    t.end()  # Stop counter and print result

    t.timerConfig(60)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    testing_loop(30000000)
    #####
    t.end()  # Stop counter and print result
    #####

    t.timerConfig(1)  # Set timer display configuration
    t.retrieveLastResult()  # Retrieve and print last timer result


#######################
if __name__ == '__main__':
    main()
