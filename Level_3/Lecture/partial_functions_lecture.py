# partial functions lectures
import functools

def power(num, exp):
    return num**exp

def main():
    # hold the exponent constant
    # need to use the kwargs so that 5 is not passed into num
    fifthPower = functools.partial(power, exp = 5)
    print(power(2,8))

    print(fifthPower(3))




#######################
if __name__ == '__main__':
    main()