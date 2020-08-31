'''
Type: Homework
Level: 1
Section: 1.6 Packages
Exercise: 2
Description: Create a main.py, in the base folder, which contains a main function.
             This module should import all the other created modules and demonstrate their functionality.
             You should use a mix of full-module imports and selective importing.
'''

# Full module import
## Import module that print "Hello World!"
## Base\Sub1\SubSub1\SubSubSub1\
import hellobye_world_demo_print_n_nextline.hellobye_world_demo_print.\
        hello_world_print.hello_world_print

## Import module that print "Bye World!"
## Base\Sub1\SubSub1\
import hellobye_world_demo_print_n_nextline.hellobye_world_demo_print.\
        bye_world_print

## Import module that print "Hello World!" with "World!" in the next line
## Base\Sub1\SubSub2\SubSubSub1\
import hellobye_world_demo_print_n_nextline.hellobye_world_demo_nextline.\
        hello_world_nextline.hello_world_nextline

## Import module that print "Bye World!" with "World!" in the next line
## Base\Sub1\SubSub2\
import hellobye_world_demo_print_n_nextline.hellobye_world_demo_nextline.\
        bye_world_nextline

## Import module that print "Hello Thanos!"
## Base\Sub1\
import hellobye_world_demo_print_n_nextline.hello_thanos




#############################################
# Selective module import

## Import module that take user input and print
## Base\Sub2\SubSub1\SubSubSub1\
from hello_world_take_input.take_input_triangle.take_input.take_input import take_input

## Import module that take user input of base, height of triangle and print its area
## Base\Sub2\SubSub1\
from hello_world_take_input.take_input_triangle.triangle import triangle

## Import module that print 'Hello World' with a tab between the 2 words
## Base\Sub2\SubSub2\SubSubSub1\
from hello_world_take_input.hellobye_world_demo_tab.hello_world_demo_tab.\
        hello_world_demo_tab import hello_world_demo_tab

## Import module that print 'Bye World' with a tab between the 2 words
## Base\Sub2\SubSub2\
from hello_world_take_input.hellobye_world_demo_tab.bye_world_demo_tab import bye_world_demo_tab

## Import module that print the word "Tony"
## Base\Sub2\
from hello_world_take_input.tony import tony




def main():
    print('Demonstrating functionalities of imported modules:\n')

    ######################################################################
    # Print "Hello World!"
    print('From: Base\Sub1\SubSub1\SubSubSub1')
    hellobye_world_demo_print_n_nextline.hellobye_world_demo_print.\
        hello_world_print.hello_world_print.hello_world_print()
    print()

    # Print "Bye World!"
    print('From: Base\Sub1\SubSub1')
    hellobye_world_demo_print_n_nextline.hellobye_world_demo_print.\
        bye_world_print.bye_world_print()
    print()

    # Import module that print "Hello World!" with "World!" in the next line
    print('From: Base\Sub1\SubSub2\SubSubSub1')
    hellobye_world_demo_print_n_nextline.hellobye_world_demo_nextline. \
        hello_world_nextline.hello_world_nextline.hello_world_nextline()
    print()

    # Import module that print "Bye World!" with "World!" in the next line
    print('From: Base\Sub1\SubSub2')
    hellobye_world_demo_print_n_nextline.hellobye_world_demo_nextline. \
        bye_world_nextline.bye_world_nextline()
    print()

    # Print "Hello Thanos"
    print('From: Base\Sub1')
    hellobye_world_demo_print_n_nextline.hello_thanos.hello_thanos()
    print()

    ######################################################################
    print('Demonstrating functionalities of imported modules using selective importing:\n')

    # Import module that take user input and print
    print('From: Base\Sub2\SubSub1\SubSubSub1')
    take_input()
    print()

    ## Import module that take user input of base, height of triangle and print its area
    print('From: Base\Sub2\SubSub1')
    triangle()
    print()

    ## Import module that print 'Hello World' with a tab between the 2 words
    print('From: Base\Sub2\SubSub2\SubSubSub1')
    hello_world_demo_tab()
    print()

    ## Import module that print 'Bye World' with a tab between the 2 words
    print('From: Base\Sub2\SubSub2')
    bye_world_demo_tab()
    print()

    ## Import module that print the word "Tony"
    print('From: Base\Sub2')
    tony()

#######################
if __name__ == '__main__':
    main()