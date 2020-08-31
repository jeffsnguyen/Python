'''
Type: Homework
Level: 1
Section: 1.1 Variables/ Conditionals
Exercise: 6
Description: Create a program that takes two inputs from the user (using input):
            The base and height of a triangle. Output should be the area of the triangle.
            As input returns a string in all cases, you’ll need to convert it to a number using float.
            Be sure to have if statements which check that the input values are valid
                for the sides of a triangle (if not, print an error message to the user).
'''

def triangle():
    # Collect base, height input from user, terminate if there is not two value entered
    while True:
        try:
            base, height = input('Input value of base and height of the triangle (separate by space): ').split()
            break
        except:
            print('Must enter 2 values.')
            continue

    # Check if the inputs are numbers, terminate if not

    base = float(base)
    height = float(height)

    # Output area of triangle
    print('Triangle area = ', abs(base) * abs(height) / 2)  # Area = base*height/2

def main():
    triangle()

#######################
if __name__ == '__main__':
    main()