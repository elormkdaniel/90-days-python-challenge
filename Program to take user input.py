# Program to take user input for a number with error handling

while True:
    try:
        # Prompt the user for input
        user_input = input("Enter a number: ")

        # Attempt to convert the input to a number
        number = float(user_input)
        print(f"You entered the number: {number}")
        break  # Exit the loop if input is valid
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid number.")
