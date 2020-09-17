# Type: Homework
# Level: 3
# Section: 3.4: Context Managers
# Exercise: 1
# Description: Contains the tests for input outputting via files
#   Open a file and write to it, using the with statement. Verify that the file has indeed been closed,
#   once the with statement exits (check the closed attribute on the file handle variable).

#######################
# Importing necessary packages

#######################

###############################################

###############################################
def main():

    # try-except block to catch errors
    try:
        with open("babyShark.txt", 'w') as f:  # open file
            f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
    except IOError as ioEx:  # catch input output error
        print(ioEx)
        pass
    except Exception as Ex:   # catch other unanticipated error
        print(Ex)
        pass
    # context manager automatically clean up after itself, no need to close the file

    print('Has the file been closed? ', f.closed)

###############################################

#######################
if __name__ == '__main__':
    main()