#Task 1: Calculate Factorial Using a Function

'''def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

# Input from user
n = int(input('Enter a number: '))

# Call the function and print result
result = factorial(n)
print("Factorial of", n, "is:", result)'''


#Task 2: Using the Math Module for Calculations
import math
n=float(input("Enter a number: "))
sqrt_value = math.sqrt(n)
log_value = math.log(n)
sine_value = math.sin(n)

# Show results
print("Square root:", sqrt_value)
print("Natural log:", log_value)
print("Sine value:", sine_value)
