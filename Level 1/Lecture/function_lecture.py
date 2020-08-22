'''
function lecture
'''

def MyFunction(name, age= None, height = None):
    print(name)
    if age:
        print(age)
    else:
        print('Unknown age!')

    if height:
        print(height)
    else:
        print('Unknown height')

def MyFunction2(name, age, *args): # args means undefined number of arguments for the function
    print(name, age)
    for i,arg in enumerate(args):
        print('arg' + str(i) + ': ' + str(arg))

def main():
    #Code goes here
    MyFunction('Sara')

    MyFunction2('Ned', 29, 69, 'New York')


#######################
if __name__ == '__main__':
    main()