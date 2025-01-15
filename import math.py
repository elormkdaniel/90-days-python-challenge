import math

# Function to calculate the square root
def calculate_square_root():
    try:
        # Ask the user for input
        number = float(input("Enter a number to find its square root: "))
        
        if number < 0:
            print("Error: Cannot calculate the square root of a negative number.")
        else:
            # Calculate the square root
            square_root = math.sqrt(number)
            print(f"The square root of {number} is {square_root:.2f}")
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a numeric value.")

# Call the function
calculate_square_root()
