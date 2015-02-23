import numpy as np
import matplotlib.pyplot as pl

def f(x):
    return np.exp(-x**2)

def main():
    N = 100000
    x = np.arange(N,dtype=np.float)

    x[0] = 0.2
    counter = 0
    for i in range(0, N-1):
        
        x_next = np.random.normal(x[i], 1.)
        if np.random.random_sample() < min(1, f(x_next)/f(x[i])):
            x[i+1] = x_next
            counter = counter + 1
        else:
            x[i+1] = x[i]

    print("acceptance fraction is ", counter/float(N))

    pl.hist(x, bins=50, color='blue')
    pl.show()

if __name__ == '__main__':
    main()
