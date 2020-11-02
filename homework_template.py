# Calculation

def factorial(x):
    i = 1
    fac = 1
    if x == 0:
        return 1
    else:
        while i <= x:
            fac = fac*i
            i += 1
    return fac


def n_choose_k(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))


def main():
    k = 1000
    sum = 0
    while k <= 2000:
        sum += ((n_choose_k(1000, 2000-k))*(n_choose_k(3000, k))/(n_choose_k(4000,2000))) * ((5000-k)/6000)
        k += 1
    print(f'The result is {sum}')



#######################
if __name__ == '__main__':
    main()