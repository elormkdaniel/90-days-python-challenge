# Function to calculate the factorial of a number
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Ask the user for input
number = int(input("Enter a number to find its factorial: "))

# Call the function and display the result
print(f"The factorial of {number} is {factorial(number)}.")
