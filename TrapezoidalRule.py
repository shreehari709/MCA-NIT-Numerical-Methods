# Program to implement the Trapezoidal Rule for a known function

# Define the function to integrate
def f(x):
    return x**2  # Example: f(x) = x^2

# Trapezoidal Rule implementation
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

# Input values
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (n): "))

# Calculate and display the result
result = trapezoidal_rule(a, b, n)
print(f"The approximate value of the integral is: {result}")