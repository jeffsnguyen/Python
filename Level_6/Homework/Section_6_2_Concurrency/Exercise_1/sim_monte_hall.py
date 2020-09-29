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
import random
import multiprocessing
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='w', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################

# Function to process the iteration
def doWork(input, output):  # 2 parameters input queue and output queue
    while True:  # Infinite loop
        try:  # this try-except is how we can know when execution is finished
            # Each loop call get playGame(), the function that play 1 iteration of the MonteHall game
            # args in this case is False, representing the Switch strat being play from the input_queue
            playGame, args = input.get(timeout=1)
            res = playGame(*args)  # call playGame() with the list of arguments
            output.put(res)  # get the result from playGame() and put it on the output queue
        except:
            break


# Play the Monte Hall game
def playGame(stayStrat):
    player = Player()
    game = Game(player)
    # Start Game
    # Player Turn 1
    player_firstChoice = player.firstPlayerSelect()  # Player select first door to open
    game.get_firstPlayerSelect(player_firstChoice)  # Host save player selection

    # Host Turn
    host_choice = game.open_firstHostSelect()  # Host select first door to open
    player.get_firstHostSelect(host_choice)  # Player save host's selection

    # Player Turn 2 (final)
    # stayStrat is a given boolean parameter
    finalChoice = player.secondPlayerSelect(stayStrat)  # Player select second door to open
    game.get_secondPlayerSelect(finalChoice)  # Host save player selection

    return game.checkResult(finalChoice)


###############################################
def main():
    # Note:
    # Stay Strat (True): At 10,000,000 iterations took total 137.37805318832397 seconds on a single process.
    # Switch Strat (False): At 10,000,000 iterations took 169.34680581092834 total on a single process.

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    # Test 1
    # Test Switch Strategy using Multiprocessing
    # Playing game in a loop
    # 5 processes, each run 2,000,000 iterations for a total 10,000,000 iterations.
    print('Test 1')
    print('Test Switch Strategy using Multiprocessing.')

    random.seed()
    numProcess = 100
    parentIteration = 100000 # Total number of iterations the game should be play

    # Create input/output queue
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    for i in range(parentIteration):
        # Each item in the queue to have a tuple of a function playGame
        #   and a list of arguments (boolean value False in this case, representing Switch strat being played)
        input_queue.put((playGame, (False,)))

    total_startTime = time()

    # Create 5 child processes
    for i in range(numProcess):  # Loop 5 times to create 5 child processes
        # target = doWork is the function for the process to call. doWork handling processing of the iterations
        # args = arguments to get passed to the target = doWork(), boolean value False in this case
        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()

    # Create an infinite loop and monitor output queue
    resultList = []

    while True:
        r = output_queue.get()  # Take something off the queue, if queue has nothing, it will block (wait)
        # until the queue has something, while other processes running in the background
        # when it has something, add it to the list resultList = []
        resultList.append(r)  # When done, break the loop
        if len(resultList) == parentIteration:
            break

    total_endTime = time()

    print(f'Final result list has {len(resultList)} items.')
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print(f'Took {total_endTime - total_startTime} seconds to run.')
    print()
    ###############################################

    # Based on the repetition result, reject the null hypothesis: probability of winning by staying is not equal
    # the probability of winning by switching.
    # One should always switch to get a higher chance at winning.
###############################################


#######################
if __name__ == '__main__':
    main()
