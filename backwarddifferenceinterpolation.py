#WAP to implement Newton's backward difference interpolation formula.
def newton_backward_interpolation(x_val, y_val, x):
    n = len(x_val)
    diff_table = [[0 for _ in range(n)] for _ in range(n)]
    

    for i in range(n):
        diff_table[i][0] = y_val[i]
    
  
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]
    
   
    h = x_val[1] - x_val[0]
    u = (x - x_val[-1]) / h
    result = y_val[-1]
    
    u_term = 1
    fact = 1
    
    for i in range(1, n):
        u_term *= (u + (i - 1))
        fact *= i
        result += (u_term * diff_table[-1][i]) / fact
    
    return result


x_val = [1891, 1901, 1911, 1921, 1931]
y_val = [46, 66, 81, 93, 101]
x = 1925


estimated_value = newton_backward_interpolation(x_val, y_val, x)
print(f"The estimated value of f({x}) is {estimated_value:.5f}")