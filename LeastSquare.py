import numpy as np

#1. WAP to fit a regression line of Y on X through a set of points using method of least squares
#2. Program to implement Simpson's (1/3) rd rule for tabulated functions
#3.Write a program to implement Trapezoidal rule for known function
# Function to calculate the regression line
#.Spline interpolation: linear, quadratic ,cubic
def least_squares_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
    m = numerator / denominator
    c = y_mean - m * x_mean
    
    return m, c


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])


m, c = least_squares_regression(x, y)

print(f"The regression line is: Y = {m:.2f}X + {c:.2f}")