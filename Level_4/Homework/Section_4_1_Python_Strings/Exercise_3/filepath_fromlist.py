# Type: Homework
# Level: 4
# Section: 4.1 Python Strings
# Exercise: 3
# Description: Contains the tests for various filepath operations
#   Create a list as follows: [‘C:’, ‘Users’, ‘Me’, ‘Desktop’, ‘MyTable.csv’]. Perform the following:
#       a. Join the list together to create a valid pathname.
#       b. Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ and join the
#           resulting list to create a valid pathname.
#######################
# Importing necessary packages

#######################

###############################################

###############################################
def main():

    fp_elements = ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']

    # a. Join the list together to create a valid pathname.
    print('a. Join the list together to create a valid pathname.')
    fp = '\\'.join(fp_elements)  # join the elements together to create the filepath
    print(fp)
    print()

    # b. Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ and join the
    #       resulting list to create a valid pathname.
    print('b. Insert another folder into the list, between ‘Desktop’ and ‘MyTable.csv’ '
          'and join the resulting list to create a valid pathname.')
    fp_elements.insert(4, 'Another_Folder')  # Insert the new folder name to file path elements list
    print(fp_elements)  # print the file path
    fp = '\\'.join(fp_elements)  # join the elements together to create the filepath
    print(fp)


###############################################

#######################
if __name__ == '__main__':
    main()
