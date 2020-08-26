'''
Type: Homework
Level: 1
Section: 1.1 Variables/ Conditionals
Exercise: 5
Description: Create a program that takes input from the user
                (using the input function), and stores it in a variable.
                and display the type of the variable that contains the value that the user entered.
'''

def main():
    var = input('Input anything: ') # Take user's input and store in variable var
    print(type(var)) # Print type of the input variable var

#######################
if __name__ == '__main__':
    main()