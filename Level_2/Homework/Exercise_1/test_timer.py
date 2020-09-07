# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 1
# Description: This contains the test function for the class Timer
#   We’ve been using time.time before and after code blocks to report the difference as the ‘time taken’.
#   This exercise is to generalize and encapsulate this into a class, to make things cleaner and reusable.
#   The steps are as follows:
#       a. Create a class called Timer.
#       b. Add a start method and end method. They should work as follows:
#               t = Timer()
#               t.start()
#               # Lots of code here
#               t.end() # This should stop the timer and print the time taken
#       c. Note that start should give an error if the Timer is already started and end should give an error
#           if the Timer is not currently running.
#       d. Add a method to retrieve the last timer result.
#       e. Add the ability to configure the Timer to display either seconds, minutes, or hours.
#           The timer result (i.e. from end and retrieveLastResult) should use whatever the current configuration is.
#       f. Test your class thoroughly.
#   This is obviously cleaner than the previous approach of subtracting times everywhere.
#   The remaining downside to this class is that one must still explicitly invoke t.start() and t.end()
#   around the code one wishes to time. We will remedy this when we extend this class using
#   context managers and decorators (see Levels 3 and 5) to make things even cleaner syntactically.

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
