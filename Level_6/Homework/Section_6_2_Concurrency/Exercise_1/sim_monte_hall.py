# Type: Homework
# Level: 6
# Section: 6.2: Concurrency
# Exercise: 1
# Description: Contains the code to simulate the Monte Hall problem, using multiprocessing
#   In this exercise, we will look to make the Monty Hall simulation achieve true multi-processing. This is
#       a good segue to financial Monte Carlo as the concepts and approaches are the same.
#
#   a) Create and initialize five processes. Note that starting processes takes some time, and is the
#       upfront cost of using multi-processing.
#   b) Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each).
#   c) Combine the five returned results lists and take the average, to get the overall result.
#   d) Time all of the above (starting from b). Does total runtime improve from the previous level?
#   e) Try decreasing/increasing the number of processes to determine the optimal runtime.
#
#   BONUS: Try the above using multithreading and compare/contrast the performance vs. multiprocessing.

#######################
# Importing necessary packages
from time import time
import logging
from montehall.player import Player
from montehall.game import Game
import multiprocessing
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


# Function to process the iteration
def doWork(input, output):  # 2 parameters input queue and output queue
    while True:  # Infinite loop
        try:  # this try-except is how we can know when execution is finished
            # Each loop call get playGame(), the function that play 1 iteration of the MonteHall game
            # args in this case is False, representing the Switch strat being play from the input_queue
            f, args = input.get(timeout=1)
            res = f(*args)  # call playGame() with the list of arguments
            output.put(res)  # get the result from playGame() and put it on the output queue
        except:
            break


###############################################
def main():
    # Note:
    # Stay Strat (True): At 10,000,000 iterations took total 88.8419759273529 seconds on a single process.
    # Switch Strat (False): At 10,000,000 iterations took 116.31930994987488 total on a single process.

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    # Test 1
    # Test Switch Strategy using Multiprocessing
    # Playing game in a loop
    # 5 processes, each run 2,000,000 iterations for a total 10,000,000 iterations.
    logging.info('###############################################')
    print('Test 1')
    print('Test Switch Strategy using Multiprocessing.')
    player1 = Player()
    game1 = Game(player1)
    numProcess = 10
    parentIteration = 10000000  # Total number of iterations the game should be play
    childIteration = int(parentIteration/numProcess)
    logging.debug(f'Running {parentIteration} iterations of the game.')

    ####################
    # Create input/output queue
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    ####################
    total_startTime = time()

    # Create child processes
    for i in range(numProcess):
        input_startTime = time()
        for j in range(childIteration):
            # Each item in the queue to have a tuple of a function playGame
            #   and a list of arguments (boolean value False in this case, representing Switch strat being played)
            input_queue.put((game1.playGame, (False,)))
        input_endTime = time()
        logging.debug(f'Input queue creation timing: {input_endTime - input_startTime} seconds.')

        process_startTime = time()
        # target = doWork is the function for the process to call. doWork handling processing of the iterations
        # args = arguments to get passed to the target = doWork(), boolean value False in this case
        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()
        process_endTime = time()
        logging.debug(f'Took {process_endTime - process_startTime} to create 1 process.')
    ####################

    # Create an infinite loop and monitor output queue
    resultList = []
    append_startTime = time()
    while True:
        if len(resultList) == parentIteration:
            break
        else:
            r = output_queue.get()  # Take something off the queue, if queue has nothing, it will block (wait)
            # until the queue has something, while other processes running in the background
            # when it has something, add it to the list resultList = []
            resultList.append(r)  # When done, break the loop
    append_endTime = time()

    logging.debug(f'Took {append_endTime - append_startTime} to append to list.')
    total_endTime = time()

    print(f'Final result list has {len(resultList)} items.')
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print(f'Took {total_endTime - total_startTime} seconds to run.')
    print()
    ###############################################

    # It's not faster. It's significantly slower.
    # I tried to optimize the Game and Player base class and reduced non-currency run time by 40%.
    # When I applies concurrency, it takes even longer than pre-optimization (because of added cost to input_queue.put()
    # See below. Total joke.......
    #
    # I've noticed that pre-optimization, when the playGame() function sits outside the class and just call
    #   functions to get selection from inside the class, it takes minimal time to create the input_queue. This is not
    #   the case post optimization when playGame() is put inside the Game class, input_queue.put takes
    #   significantly longer (minimum 10x longer). And of course the output_queue.get doesn't sit inside a process
    #   so there's no performance to be had there.
    #
    # Speaking of: the most expensive part of the code is the while() loop to get from the queue. No improvement here
    # because it sits outside of the processes. I have no idea how to fix this.
    #
    # To answer e) There's no improvement from 5 processes (about 800 seconds) to 10 processes (935 seconds).
###############################################


#######################
if __name__ == '__main__':
    main()
