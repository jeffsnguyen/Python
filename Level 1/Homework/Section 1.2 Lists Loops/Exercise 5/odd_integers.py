'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 4
Description: Create a list of all odd integers 1-1000.
             Write a loop that prints all numbers in the above list, separated by commas.

'''

# Initialize list of odd integers in the range of n[1,1000]
def odd_integers():
    return [num for num in range(1,1001) if num % 2 != 0]

def main():

    # Call odd_integers and save to list_odd
    list_odd = odd_integers()

    # Display list using a loop, as requested by the exercise
    i = 1 # Initialize count variable
    print_list = str(list_odd[0]) # Initialize a list with first position of list_odd
    while i < len(list_odd):
        print_list = print_list + ', ' + str(list_odd[i]) # Append list item to print_list
        i += 1

    # Display list
    print(print_list)

#######################
if __name__ == '__main__':
    main()