import numpy as np
import numba

@numba.jit(nopython=True)
def gaussian_kernel_function(Y1, Y2, sigma):
    return np.exp(-np.linalg.norm(Y1 - Y2)**2 / (2 * sigma**2))