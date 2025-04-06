import numpy as np

def gauss_forward_interpolation(x_values, y_values, x):
    n, h = len(x_values), x_values[1] - x_values[0]
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for j in range(1, n):
        diff_table[:n-j, j] = diff_table[1:n-j+1, j-1] - diff_table[:n-j, j-1]

    u, y_interpolated, u_term = (x - x_values[0]) / h, y_values[0], 1
    for i in range(1, n):
        u_term *= (u - (i - 1)) / i
        y_interpolated += u_term * diff_table[0][i]

    return y_interpolated

x_values, y_values, x = np.array([1, 2, 3, 4, 5]), np.array([1, -1, 1, -1, 1]), 3.5
print(f"The interpolated value at x = {x} is {gauss_forward_interpolation(x_values, y_values, x)}")
