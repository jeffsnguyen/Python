# multiprocessing lecture

import multiprocessing
import random
import time

def calculate(f, args):
    return f(*args)

def doWork(input, output):  # 2 parameters input queue and output queue
    while True:  # Infinite loop
        try:  # this try-except is how we can know when execution is finished
            f, args = input.get(timeout=1)  # Each loop call get
                                            # f is the function f()
                                            # args in this case is random.random() from the input_queue
            res = f(*args)  # call f() with the list of arguments
            output.put(res)  # get the result from f() and put it on the output queue
        except:
            output.put('Done')  # Put the word 'Done' in the output queue
            break

def f(a):  # runSim (for monte hall problem)
    time.sleep(1)  # run simulation
    return a  # In Monte Hall simulation, return the actual result

def main():

    input_queue = multiprocessing.Queue()   # Create a Queue type object, anything can be added to the queue
    output_queue = multiprocessing.Queue()  # and communicate to each other
    # In this case, output contains the results from the function
    # Input = all the functions the process to do



    # Put on a Queue -> add something (variable, type, string) to the queue
    # Get from a Queue -> remove from the queue
    # Order is FIFO, first thing get put to the queue is the first thing taken off the queue
    # Stack is LIFO

    for i in range(50):
        # Each item in the queue to have a tuple of a function f and a list of arguments (in this case a random value)
        # Because f() only need 1 parameters, only pass 1 random.random in the tuple
        # If f need 2, the tuple will need 2, for example: (random.random(), 2)
        # Pass in random.random() in this case so the function is similar to Monte Hall problem
        input_queue.put((f, (random.random(),)))

    s = time.time()

    # Create processes
    for i in range(50):  # Loop 5 times to create 5 child processes, too many will crash computer
        # target = doWork() is the function you want the process to call
        # args = arguments to get passed to the target = doWork()
        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()

    # as soon as the process is started, the target = doWork() function gets called

    # Create an infinite loop and monitor output queue
    res = []
    while True:
        r = output_queue.get()  # Take something off the queue, if queue has nothing, it will block (wait)
                                # until the queue has something, while other processes running in the background
                                # when it has something, add it to the list res = []
        if r != 'Done':
            res.append(r)   # When done, break the loop
        else:
            break

    e = time.time()
    print(len(res))
    print(res)
    print(f'Time taken: {e-s}')
#######################
if __name__ == '__main__':
    main()
