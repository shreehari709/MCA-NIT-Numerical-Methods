import numpy as np

def backward_difference_table(fx):
    n = len(fx)
    table = np.zeros((n, n))
    table[:, 0] = fx
    for j in range(1, n):
        table[j:, j] = table[j:, j-1] - table[j-1:-1, j-1]
    return table

def gauss_backward_interpolation(x, fx, x0):
    h, u = x[1] - x[0], (x0 - x[-1]) / (x[1] - x[0])
    table = backward_difference_table(fx)
    result, term = table[-1, 0], 1
    for i in range(1, len(x)):
        term *= (u + i - 1) / i
        result += term * table[-1, i]
    return result

x = np.array([1940, 1950, 1960, 1970, 1980, 1990])
fx = np.array([17, 20, 27, 32, 36, 38])
x0 = 1976
print(f"The interpolated value at x = {x0} is: {gauss_backward_interpolation(x, fx, x0)}")
