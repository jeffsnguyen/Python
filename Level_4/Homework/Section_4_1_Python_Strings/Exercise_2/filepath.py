# Type: Homework
# Level: 4
# Section: 4.1 Python Strings
# Exercise: 1
# Description: Contains the tests for various strings operations
#   Save the following Windows file-path into a string variable: C:\Users\Me\Desktop\MyTable.csv.
#
#   Perform the following operations:
#       a. Extract the filename with extension from the path.
#       b. Extract the file extension only.
#       c. Add another folder (can name it whatever you’d like) between ‘Desktop’ and the filename.
#######################
# Importing necessary packages

#######################

###############################################

###############################################
def main():

    fp = 'C:\\Users\Me\\Desktop\\MyTable.csv'

    # a. Extract the filename with extension from the path.
    print('a. Extract the filename with extension from the path.')
    print(fp.split('\\'))
    print()

    # a. Extract the filename with extension from the path.
    print('a. Extract the filename with extension from the path.')
    print(fp.split('\\'))
    print()


###############################################

#######################
if __name__ == '__main__':
    main()