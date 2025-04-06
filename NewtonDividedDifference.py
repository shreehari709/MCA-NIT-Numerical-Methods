#1. Find Solution using Newton's Divided Difference Interpolation formula
#x = [300,304,305,307]	f(x) = [2.4771,2.4829,2.4843,2.4871] , x = 301
def newton_divided_difference(x, y, value):
    n = len(x)
   
    diff_table = [[0 for _ in range(n)] for _ in range(n)]
    
  
    for i in range(n):
        diff_table[i][0] = y[i]
    
   
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (x[i + j] - x[i])
    
    
    result = diff_table[0][0]
    product = 1
    for i in range(1, n):
        product *= (value - x[i - 1])
        result += product * diff_table[0][i]
    
    return result


x = [300, 304, 305, 307]
y = [2.4771, 2.4829, 2.4843, 2.4871]
value = 301


result = newton_divided_difference(x, y, value)
print(f"The interpolated value at x = {value} is {result}")