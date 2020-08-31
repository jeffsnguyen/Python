'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 6
Description: Create an alternative mean function to use *args instead of a taking a list of numbers.
             It should be invoked as follows (for example):

             argsMean(1.3, 4.5, 6.7, 11.2, 100, 987.6)

             Test the function with variable numbers of arguments.
             It’s also possible to pass a list or tuple into this version of the function
                by using the * operator – you should attempt this as well.
'''

# Return mean value of a variable number of arguments
def argsmean(*args):
    return sum(args)/ len(args)

def main():
    # Display mean
    print('Mean = ' + str(argsmean(10, 10)))


#######################
if __name__ == '__main__':
    main()