# numerical packages  lecture

import numpy_financial
import numpy as np
import time
from utils.timer import Timer
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

def main():
    nps = []
    pyts = []

    dataNP = np.random.random(1000000)
    dataPyt = list(dataNP)

    for i in range(1, 1000000, 10000):
        s = time.time()
        dataNP[0:i + 1].sum()
        dataNP
        e = time.time()
        timeTaken = e - s
        nps.append(timeTaken)

        s = time.time()
        sum(dataPyt[0:i + 1])
        e = time.time()
        timeTaken = e - s
        pyts.append(timeTaken)

    nps = gaussian_filter(nps, sigma=5)
    pyts = gaussian_filter(pyts, sigma=5)

    x = np.arange(1, 1000000, 10000)

    plt.figure(figsize=(20, 10))
    plt.plot(x, nps, label='NumPy')
    plt.plot(x, pyts, label='Python')
    plt.grid()
    plt.legend()
    plt.show()


#######################
if __name__ == '__main__':
    main()
