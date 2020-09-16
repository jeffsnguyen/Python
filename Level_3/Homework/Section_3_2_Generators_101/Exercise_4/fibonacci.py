# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 4
# Description: Contains the tests to modified fn() method to generate Fibonacci sequence
#   Modify the Fibonacci function from Exercise 1.3.2 to be a generator function. Note that the function
#       should no longer have any input parameter since making it a generator allows it to return the
#       infinite sequence. Do the following:
#           a. Display the first and second values of the Fibonacci sequence.
#           b. Iterate through and display the next 100 values of the sequence.

#######################
# Importing necessary packages


#######################

###############################################

# Fibonacci generator
def fn():
    fibo = [] # Initialize empty list
    num = -1 # Set count value

    # For the first 2 values, yield specific constants and append to empty list
    # For subsequent values, yield using fibonacci formula and append to list
    while True:
        num += 1
        if num == 0:
            yield 0
            fibo.append(0)
        elif num == 1:
            yield 1
            fibo.append(1)
        else:
            yield fibo[num-2] + fibo[num-1]
            fibo.append(fibo[num-2] + fibo[num-1])

###############################################
def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test modified fn() function by printing out the first 2 value of Fibonacci sequence
    #       2. Test modified fn() function by printing out the next 100 value of Fibonacci sequence

    ###############################################

    # Test 1
    # 1.1 Test modified fn() function by printing out the first 2 value of Fibonacci sequence
    print('Test 1.1. Printing out the first 2 value of Fibonacci sequence')

    fib = fn()
    print(next(fib))
    print(next(fib))
    print()

    # 1.2 Test modified fn() function by printing out the next 100 value of Fibonacci sequence (#3 to #102)
    print('Test 1.2. Test modified fn() function by printing out the next 100 value of Fibonacci sequence (#3 to #102)')

    for i in range (0,101):
        print(next(fib))
        i +=1

###############################################

#######################
if __name__ == '__main__':
    main()