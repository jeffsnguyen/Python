'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 3
Description: Create a function that calculates the mean of a passed-in list.
'''

# Return mean value of a list
def mean(list):
    return sum(list)/ len(list)

def main():
    l = [1, 2, 3]
    print('Mean = ' + str(mean(l)))


#######################
if __name__ == '__main__':
    main()