#  context managers lectures

class TestContextManager(object):
    def __init__(self, msg):
        self.msg = msg

    def __enter__(self):
        print('The context has been entered...')
        return self.msg

    def __exit__(self, *args):
        print(args[0])
        print(args[1])
        print(args[2])
        print('The context is exiting')

def main():
    f = open("regular.txt", 'w')
    f.write('Python is awesome!')
    # If error happens here, program terminate -> file doesn't get close -> memory leak
    f.close()

    with open("contextManager.txt", 'w') as f:
        f.write('Python is even better with context managers!')
    # context manager automatically clean up after itself, no need to close the file

    #Example
    #with time():
    #   code here


    with TestContextManager('Hello') as msg:
        print(msg)
        print('Inside context manager block')
#######################
if __name__ == '__main__':
    main()