'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 3
Description: Create a list of unique mortgage amounts.
'''

import random

def main():
    # Generate the list  of 100 mortgages from 100000 to 1000000 using random sample to ensure uniqueness
    mortgage = list(random.sample(range(100000, 1000000), 100))
    # Display the lsit
    print(mortgage)

#######################
if __name__ == '__main__':
    main()