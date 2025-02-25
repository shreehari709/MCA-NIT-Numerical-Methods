# 2) WAP to implement Newton's forward difference interpolation formula.
def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    diff_table = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the first column with given y values
    for i in range(n):
        diff_table[i][0] = y_values[i]
    
    # Calculate forward differences
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    
    # Calculate the interpolation result
    h = x_values[1] - x_values[0]
    u = (x - x_values[0]) / h
    result = y_values[0]
    
    u_term = 1
    fact = 1
    
    for i in range(1, n):
        u_term *= (u - (i - 1))
        fact *= i
        result += (u_term * diff_table[0][i]) / fact
    
    return result

# Given data points
x_values = [1891, 1901, 1911, 1921, 1931]
y_values = [46, 66, 81, 93, 101]
x = 1895

# Compute interpolation
estimated_value = newton_forward_interpolation(x_values, y_values, x)
print(f"The estimated value of f({x}) is {estimated_value:.5f}")