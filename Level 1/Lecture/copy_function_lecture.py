'''
function lecture
'''
import copy
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

def MyFunction2(name, age, *args):
    print(name, age)
    for i,arg in enumerate(args):
        print('arg' + str(i) + ': ' + str(arg))

def MyFunction3(name, age, *args, **kwargs):
    # keyword args: kwargs is a dictionary: python type that hold value in
    #the form key to value
    print(name, age)
    print(kwargs.get('state')) #get the value for the key 'state'
    print(kwargs.get('height'))
    print(kwargs.get('weight'))

def CheckParameterMod(input):
    copiedInput = copy.copy(input) #splice or create a copy of original list
    #deecopy used when you have a list of list
    copiedInput[0] = 8
    copiedInput.append(88)
    print(copiedInput)

def main():
    #Code goes here
    #MyFunction('Sara')

    #MyFunction2('Ned', 29, 69, 'New York')
    MyFunction3('Ned', 29, height=69, state='New York') #note that state was not specified in the def

    i = [1,5,7,6,9]
    CheckParameterMod(i) #Be careful to not modify data.
    print(i)

#######################
if __name__ == '__main__':
    main()