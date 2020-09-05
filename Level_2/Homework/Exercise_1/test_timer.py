## Type: Homework
## Level: 1
## Section: 2.1: Classes
## Exercise: 1
## Description: This contains the test function for the class Timer

from utils.timer import Timer
import threading
import time

def main():
    #t = Timer(12,45,476)
    t = Timer()
    print(t.start())
    count = 0
    for i in range(1,100000000):
        count += i
    print(count)
    print(t.end())
    #print(t.hours)
    #print(t.minutes)
    #print(t.seconds)

#######################
if __name__ == '__main__':
    main()