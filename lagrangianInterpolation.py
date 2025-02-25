# 1) WAP to implement Lagrangian method of interpolation.
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result


x_values = [2, 2.5, 3]
y_values = [0.69315, 0.91629, 1.09861]
x = 2.7


estimated_value = lagrange_interpolation(x_values, y_values, x)
print(f"The estimated value of f({x}) is {estimated_value:.5f}")
