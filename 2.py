import numpy as np
def vector(x):
    y = np.zeros((len(x)*2)-1)
    y[::2] = x
    return y

x = np.array([1, 7, 8, 9, 10, 6])
print(x)
print(vector(x))

