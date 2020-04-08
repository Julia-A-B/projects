import numpy as np
def vector(x):
    y = np.zeros((len(x)*2)-1)
    y[::2] = x
    return y



