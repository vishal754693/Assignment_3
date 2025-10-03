import math

# 1. Ask the user for a number as input
number = float(input("Enter a number: "))

# 2. Use the math module to calculate:
sqrt_result = math.sqrt(number)                     # Square root
log_result = math.log(number)                       # Natural logarithm (log base e)
sine_result = math.sin(number)                      # Sine (input is in radians)

# 3. Display the calculated results
print(f"\nResults for the number {number}:")
print(f"Square root: {sqrt_result}")
print(f"Natural logarithm (log base e): {log_result}")
print(f"Sine (in radians): {sine_result}")
