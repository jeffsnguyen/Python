'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 5
Description: Do the following:
                a. Create an aggregate list from 3) and 4) and print it out, separated by commas.
                b. Print out the aggregate list, backwards and separated by commas.

'''
from even_integers import even_integers
from odd_integers import odd_integers

def main():

    # Initialize list of integers [1,1000]
    list_even = even_integers()
    list_odd = odd_integers()

    # Aggregate list
    list_agg = list_even + list_odd

    print(list_agg) # Print list

    print(list_agg[::-1]) # Print list backwards


#######################
if __name__ == '__main__':
    main()