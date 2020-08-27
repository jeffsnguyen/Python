'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 1
Description: Create a program that:
                a. Keeps asking the user for a number, until the user enters the letter s.
                b. Once the user finishes entering numbers,
                    calculate and display the average of the numbers. You should do this using a loop.

'''

def main():

    number_list = [] # Initialize an empty list to store number inputs

    # Take input from user
    # Repeat ask until letter 's' is entered
    while True:
        num = '' # Initialize empty variable to take input
                 # and refresh this every time one loop instance is completed
        while num == '':
            num = input('Add a number to the list (s to stop)): ')
        try: # exception handling of input if a different string (not number or 's') was entered
            if num != 's': # if input is not 's' then add it to the pre-initalized list
                number_list.append(float(num))
            else: # if input is 's' then break the loop
                break
        except:
            # In the event of exception, warn user and reset num value so loop may continue
            print('Input invalid: must be a number or the letter s.')
            num = ''

    sum_number = 0.0  # Initialize zero variable to store the sum of number

    # Loop to calculate sum of all entries in the list
    for num in number_list:
        sum_number += num

    avg = sum_number / len(number_list) # Calculate average

    print('Average is: ' + str(avg)) # Display result


#######################
if __name__ == '__main__':
    main()