'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 9
Description: Write a list comprehension that results in a list of all numbers 0 through 10,000,000.

             a. Using a loop, filter the resulting list,
             to create another list that only contains numbers ending with the digit 0.

             b. Do the same as a) using a list comprehension.
             Use the time.time function to capture the time taken for each version. Which is quicker? Why?
'''

import time
import pprint

def main():

    # Initialize list
    all_numbers = [num for num in range(0,10000000)]

    # Filter list to show only numbers ending with 0, using a loop
    all_numbers_zero = [] # Initialize an empty list
    start_time = time.time()
    for i in all_numbers:
        if i % 10 == 0: # If remainder of i/10 = 0 then i is divisible by 10, added to list
            all_numbers_zero.append(i)
    print("%.3f" % (time.time()-start_time))

    # Filter list to show only numbers ending with 0, using list comprehension
    start_time = time.time()
    all_numbers_end_zero = [num for num in range(0,10000000) if num % 10 == 0]
    print("%.3f" % (time.time()-start_time))
    print()

    # List comprehension is slower than loop in this instance because the for loop
    # did not have to look up the range(1, 10000000) and only look up in the
    # already established list all_numbers. The for loop would have been slower otherwise as the
    # list comprehension method does not need to look up the list and its append method ever iteration
    pprint.pprint('List comprehension is slower than loop in this instance because the for loop '
          'did not have to look up the range(1, 10000000) and only look up in the'
          'already established list all_numbers. The for loop would have been slower otherwise as the'
          'list comprehension method does not need to look up the list and its append method ever iteration.')

#######################
if __name__ == '__main__':
    main()