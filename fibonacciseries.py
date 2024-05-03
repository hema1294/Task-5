#Python program to create a Fibonacci series from 1 to 50 elements using lambda function

from functools import reduce

# Fibonacci function using lambda for the recursive logic
fibonacci = lambda n : reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

# Create Fibonacci series up to 50 elements
fibonacci_series_up_to_50 = fibonacci(50)

# Print the Fibonacci series
print("Fibonacci series up to 50 elements:", fibonacci_series_up_to_50)
