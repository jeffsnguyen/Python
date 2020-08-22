'''
looping
'''

def main():
    n = int(input('Find factorial of: '))
    result = 1

    for i in range(1, n+1):
        result *= i

    print(result)

#######################
if __name__ == '__main__':
    main()