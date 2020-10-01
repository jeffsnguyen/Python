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
from utils.timer import Timer
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


# Run the sim n time, return the list of results
def runSimList(game, stayStrat, n):
    result = []
    for i in range(n):
        result.append(game.playGame(stayStrat))

    return result


# Simply run the simulation n times and return the probability
@Timer
def runSimProbability(game, stayStrat, n):
    result = runSimList(game, stayStrat, n)
    print(f'Win probability: {sum(result) / len(result)}')


# Function to process the iteration
def doWork(input, output):  # 2 parameters input queue and output queue
    # Each loop call get playGame(), the function that play 1 iteration of the MonteHall game
    # args in this case is False, representing the Switch strat being play from the input_queue
    f, args = input.get(timeout=1)
    res = f(*args)  # call playGame() with the list of arguments
    output.put(res)  # get the result from playGame() and put it on the output queue


# Run the simulation in parallel using multiprocessing
# game is the object Game class
# stayStrat is the player strategy: {True: 'always stay', False: 'always switch'}
# nsim is number of simulations to run
# nprocess is number of process to use
@Timer
def runParalellSim(game, stayStrat, nsim, nprocess):
    # Create input/output queue
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    jobs = []  # Job list for each process
    ####################

    # Create child processes
    for i in range(nprocess):
        # Each item in the queue to have a tuple of a function runSimList
        #   and a list of arguments (boolean value False in this case, representing Switch strat being played)
        input_queue.put((runSimList, (game, stayStrat, int(nsim / nprocess))))

        # target = doWork is the function for the process to call. doWork handling processing of the iterations
        # args = arguments to get passed to the target = doWork(), boolean value False in this case
        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()
        jobs.append(p)  # Add each process to the job list
    ####################

    # Create an infinite loop and monitor output queue
    resultList = []
    while True:
        if len(resultList) == nsim:
            break
        else:
            r = output_queue.get()  # Take something off the queue, if queue has nothing, it will block (wait)
            # until the queue has something, while other processes running in the background
            # when it has something, add it to the list resultList = []
            resultList.extend(r)  # When done, break the loop

    print(f'Final result list has {len(resultList)} items.')
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')

    # Clean up crew
    for job in jobs:
        job.join()
        job.terminate()

###############################################
def main():
    # Note:
    # Stay Strat (True): At 10,000,000 iterations took total 82.36606335639954 seconds on a single process.
    # Switch Strat (False): At 10,000,000 iterations took 98.25793862342834 total on a single process.

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    # Test 1
    # Test Switch Strategy using Multiprocessing
    # Playing game in a loop
    # 5 processes, each run 2,000,000 iterations for a total 10,000,000 iterations.
    print('Test 1')
    print('Test Stay Strategy using Multiprocessing.')
    player1 = Player()
    game1 = Game(player1)

    runParalellSim(game1, False, 10000000, 20)

    print()
    ###############################################

    # d) Run time significantly improved:
    #   4 processes: 30.22 seconds
    #   5 process: 26.32 seconds
    #   10 process: 20.726064443588257 seconds
    #   20 process: 20.650052309036255
###############################################


#######################
if __name__ == '__main__':
    main()
