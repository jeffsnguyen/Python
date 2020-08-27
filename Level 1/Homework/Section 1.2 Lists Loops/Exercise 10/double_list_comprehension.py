'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 10
Description: Create a list of lists of any type. Use the double list-comprehension syntax,
             as described in the lecture, to create a flattened single list.

             Note that this can be useful in situations where one has a function
             that returns a list of items, and calls the function many times,
             resulting in a large list of lists (which can then be flattened, for simplicity).
'''

def main():

    # Initialize list
    nested_list = [[1,2,3,4,5], [3,4,6], [7,4,3,2], [1,12,13]]

    # Double list comprehension to flatten the list
    flattened_list = [item for sublist in nested_list for item in sublist]

    print(flattened_list)



#######################
if __name__ == '__main__':
    main()