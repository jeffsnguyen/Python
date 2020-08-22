'''
looping
'''

def main():
    n = int(input('Find factorial of: '))
    result = 1

    while (n>1):
        result *= n
        n -= 1

    print(result)

#######################
if __name__ == '__main__':
    main()