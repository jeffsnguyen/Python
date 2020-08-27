'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 2
Description: Write a function that returns the Fibonacci sequence as a list.
             The function should take a parameter called N
             and return the entire sequence of Fibonaccis, from 0-N.
'''
import sys

# Return fibonacci list from 0 -> n
def fn(n):
    # Initialize list with f_n0 = 0
    fibo = [0]

    if n == 0: # Check for 0 input
        return fibo
    else:
        fibo.append(1)
        for num in range(2,n):
            check = fibo[num-2] + fibo[num-1]
            # if the sum is less than or equal to n, add to list, else break the loop
            if check <= n:
                fibo.append(check)
            else:
                break
        return fibo

def main():
    print('This program print a fibonacci sequence from 0 -> input')

    # Exception handling for input others than positive integers
    try:
        n = int(input('Enter a positive integer: '))
        if n < 0:
            sys.exit('Must be a positive integer.')
    except:
        sys.exit('Must be a positive integer.')

    # Print out the sequence:
    print(fn(n))


#######################
if __name__ == '__main__':
    main()