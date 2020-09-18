# file input ouput lecture



def main():
    fp = open('Sample Loans.csv')
    print(type(fp))
    print(fp.readline())  # put the entire line in a string
    ln = fp.readline()  # put the entire line in a string. next line
    print(ln)
    print(ln.split(','))
    print(ln.strip('\n').split(','))
    print()

    fp = open('Sample Loans.csv')
    #f = fp.read()  # read entire file into a string
    #print(f)


    # Better approach
    with open('Sample Loans.csv'):  # default is to read 'r',
        for line in fp:
            print(line)

    # if the file exist, overwrite, else create a new file
    with open('Sample Loans.csv', 'w') as fp:
        fp.write('1,100000,.0050,30')

    # a = append
    with open('Sample Loans.csv', 'a') as fp:
        fp.write('\n2,200000,.0075,28')

    # file opened for writing is not able to be read
    # r+ = can read and write



#######################
if __name__ == '__main__':
    main()