'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 2
Description: Create a list of ten numbers. Should contain some integers and some decimals.
             Perform the following operations:
                a. Display the first two numbers from the list (using indexing).
                b. Display the last two numbers.
                c. Display all the numbers besides the last number, using a single print statement.
                d. Display all the numbers besides the first number, using a single print statement.
                e. Display all the numbers besides the first two and last three numbers, using a single print.
                f. Append one number to the end of the list.
                g. Append five numbers to the end of the list, using a single operation.
                h. Insert one number right after the third number in the list.
                i. Modify the fourth-to-last number in the list.
                j. Display the list backwards, using splicing.
                k. Display every second item in the list.
                l. Display every second item in the list, backwards.

'''

def main():

    number_list = [1, 2, 3, 5.5, 3, 7.7, 8.8, 1, 5.5, 10] # Initialize list of numbers

    # a. Display the first two numbers from the list (using indexing).
    print('a. Display the first two numbers from the list')
    print(number_list[:2])

    # b. Display the last two numbers.
    print('b. Display the last two numbers.')
    print(number_list[-2:])

    # c. Display all the numbers besides the last number, using a single print statement.
    print('c. Display all the numbers besides the last number, using a single print statement.')
    # If the position in the list is the last, skip print
    print(number_list[:len(number_list)-1])

    # d. Display all the numbers besides the first number, using a single print statement.
    print('d. Display all the numbers besides the first number, using a single print statement.')
    # If the position in the list is 0, or the first position, skip print
    print(number_list[1:])

    # e. Display all the numbers besides the first two and last three numbers, using a single print.
    print('e. Display all the numbers besides the first two and last three numbers, using a single print.')

    print(number_list[2:-3])

    # f. Append one number to the end of the list.
    print('f. Append one number to the end of the list.')
    number_list.append(1001)
    print(number_list)

    # g. Append five numbers to the end of the list, using a single operation.
    print('g. Append five numbers to the end of the list, using a single operation.')
    number_list.extend([2, 19, 12.4353, 12, 7])
    print(number_list)

    # h. Insert one number right after the third number in the list.
    print('h. Insert one number right after the third number in the list.')
    number_list.insert(3, 10.1313)
    print(number_list)

    # i. Modify the fourth-to-last number in the list.
    print('i. Modify the fourth-to-last number in the list.')
    number_list[-4] = 100000
    print(number_list)

    # j. Display the list backwards, using splicing.
    print('j. Display the list backwards, using splicing.')
    print(number_list[::-1])

    # k. Display every second item in the list.
    print('k. Display every second item in the list.')
    print(number_list[::2])

    # l. Display every second item in the list, backwards.
    print('l. Display every second item in the list, backwards.')
    print(number_list[::-2])


#######################
if __name__ == '__main__':
    main()