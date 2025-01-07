# Program to greet user and calculate their birth year

# Take user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate the year the user was born
current_year = 2025  # You can change this to the current year dynamically using `import datetime`
birth_year = current_year - age

# Print a greeting with the user's name and the calculated birth year
print(f"Hello, {name}! You were born in {birth_year}.")
