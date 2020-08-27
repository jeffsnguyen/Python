'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 3
Description: Create a list of all even integers 1-1000.
             Write a loop that prints all numbers in the above list, separated by commas.

'''

# Initialize list of even integers in the range of [1,1000]
def even_integers():
    return [num for num in range(1,1001) if num % 2 == 0]

def main():

    # Call even_integers and save to list_even
    list_even = even_integers()

    # Display list using a loop, as requested by the exercise
    i = 1 # Initialize count variable
    print_list = str(list_even[0]) # Initialize a list with first position of list_even
    while i < len(list_even):
        print_list = print_list + ', ' + str(list_even[i]) # Append list item to print_list
        i += 1

    # Display list
    print(print_list)

#######################
if __name__ == '__main__':
    main()