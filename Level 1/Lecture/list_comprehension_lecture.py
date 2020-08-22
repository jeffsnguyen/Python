'''
list comprehension lecture
'''

import time

def main():
    #Create list of squares of even numbers, 0-10000000
    lst = range(10000000)

    start = time.time() #time is a built in python function
    res = []
    for l in lst:
        if l%2 == 0:
            res.append(l**2)

    end = time.time()

    print('Seconds: ' + str(end-start))

    start = time.time()
    res2 = [i**2 for i in lst if i%2 == 0]
    end = time.time()

    print('Seconds: ' + str(end-start))

#######################
if __name__ == '__main__':
    main()