# decorator  lecture

import time
from functools import wraps


# decorator
def Timer(f):  # timer function
    # Nesting function
    @wraps(f)   # decorator that decorate the wrapped function to retain the representation of the function
    def wrapped(*args, **kwargs):  # take all keyword and non-keyword parameters
        s = time.time()
        result = f(*args, **kwargs)
        e = time.time()
        print(f'Function {f}: {e-s} seconds.')
        return result

    return wrapped


@Timer  # decorating the function with the Timer function
def intenseFunction(input):
    time.sleep(input)  # cause program to wait and do nothing for 5 seconds
    return 'Done'


def main():

    print(intenseFunction(5))


#######################
if __name__ == '__main__':
    main()
