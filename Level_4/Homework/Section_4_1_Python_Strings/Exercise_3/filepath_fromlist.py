# Type: Homework
# Level: 4
# Section: 4.1 Python Strings
# Exercise: 1
# Description: Contains the tests for various filepath operations
#   Save the following Windows file-path into a string variable: C:\Users\Me\Desktop\MyTable.csv.
#
#   Perform the following operations:
#       a. Extract the filename with extension from the path.
#       b. Extract the file extension only.
#       c. Add another folder (can name it whatever you’d like) between ‘Desktop’ and the filename.
#######################
# Importing necessary packages
import os

import shutil
#######################

###############################################

###############################################
def main():

    fp = 'C:\\Users\\sonje\\Desktop\\MyTable.csv'

    # a. Extract the filename with extension from the path.
    print('a. Extract the filename with extension from the path.')
    print(fp.rsplit('\\', 1)[1])
    print()

    # b. Extract the file extension only.
    print('b. Extract the file extension only.')
    print(fp.split('.')[1])
    print()

    # c. Add another folder (can name it whatever you like) between Desktop and the filename.
    print('c. Add another folder (can name it whatever you like) between Desktop and the filename.')
    fp1 = 'C:\\Users\\sonje\\Desktop\\Another_Folder\\'
    try:  # try-except block to catch if folder already exist
        os.mkdir(fp1)
    except FileExistsError as fileEEx:
        print(fileEEx)
        pass
    else:
        try:  # try-except block to catch if move can't be done
            dest = shutil.move(fp, fp1)
        except Exception as Ex:
            print(Ex)
            pass
            
    print()

###############################################

#######################
if __name__ == '__main__':
    main()