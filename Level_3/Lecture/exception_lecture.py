#  exception lectures

def mean(values):
    if not isinstance(values, (list, tuple)): # if parameter is not empty
        raise TypeError('Must be a list with at least 1 value.') # if its not a list
    elif values:
        return sum(values) / len(values)
    else:
        raise ValueError('Must be a list with at least 1 value.')

def main():
    try:
        print(mean(['a']))
    except ValueError as ex:  # store exception in the ex variable
        print(ex)
    except TypeError as ex1:
        print(ex1)
    except:
        print('Unknown error' + str(ex))
    print('Hello')

    # Duck Typing
    # Enclose in a try except block

#######################
if __name__ == '__main__':
    main()