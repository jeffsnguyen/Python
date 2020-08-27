'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 6
Description: Write a list comprehension that results in a list of the squares of all numbers 0 through 100:
             a. Filter the resulting list, to create another list
                that only contains numbers greater than 1000.
             b. Filter further, to create another list that only contains even numbers
                (hint: use the Modulus operator).

'''

def main():

    # Initialize square as list of squares of numbers 0 through 100
    squares = [i**2 for i in range(0,100)]

    # Filter squares with only number greater than 1000
    squares_1000 = [i**2 for i in range(0,100) if i**2 > 1000]

    # Filter squares_1000 with only number greater than 1000, and only even numbers
    squares_1000_even = [i**2 for i in range(0,100) if (i**2 > 1000) and (i**2 % 2 == 0)]


#######################
if __name__ == '__main__':
    main()