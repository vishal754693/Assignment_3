# 1. Define a function named factorial that takes a number as an argument
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  # 2. Returns the calculated factorial

# 3. Call the function with a sample number and print the output
sample_number = 5
output = factorial(sample_number)
print(f"The factorial of {sample_number} is: {output}")
