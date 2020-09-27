# montecarlo  lecture

import random
import time

def main():

    random.seed(1)  # Only seed it once

    print('Set 1')
    print(random.random())  # Uniformly random number between 0,1
    print(random.uniform(3, 11))  # Can specify a bound
    print()

    print('Set 2')
    random.seed(1)   # Reseed
    print(random.random())  # Uniformly random number between 0,1
    print(random.uniform(3, 11))  # Can specify a bound
    print()

    print('Set 3')
    random.seed(time.time())  # Change the time to change the seed
    print(random.random())
    print(random.randint(2, 10))  # Integer
    print()

    print('Set 4')
    l = [1, 3, 5, 8, 10]
    print(random.choice(l))  # Random number form list l
    print(random.shuffle(l))   # shuffle
    print()

    print('Set 5')
    print(random.normalvariate(50, 2))  # Normally distributed
    print()

    print(random.random()*20+30)
    print('Set 6')
#######################
if __name__ == '__main__':
    main()
