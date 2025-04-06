#Calculate Cubic Splines
#X = [	1	,2	,3	,4 ]
#Y =[1	,2	,5	,11 ] y(1.5), y'(3)

import numpy as np
from scipy.interpolate import CubicSpline, interp1d


linear_spline = interp1d(X, Y, kind='linear')
y_linear_1_5 = linear_spline(1.5)


quadratic_spline = interp1d(X, Y, kind='quadratic')
y_quadratic_1_5 = quadratic_spline(1.5)


cubic_spline = CubicSpline(X, Y)
y_cubic_1_5 = cubic_spline(1.5)
y_cubic_derivative_3 = cubic_spline(3, 1)

print("Linear Spline y(1.5):", y_linear_1_5)
print("Quadratic Spline y(1.5):", y_quadratic_1_5)
print("Cubic Spline y(1.5):", y_cubic_1_5)
print("Cubic Spline y'(3):", y_cubic_derivative_3)