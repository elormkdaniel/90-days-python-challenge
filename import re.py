import re

# Function to validate email addresses
def validate_email(email):
    # Define the regular expression for a valid email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(email_regex, email):
        return True
    else:
        return False

# Ask the user for an email address
email = input("Enter an email address to validate: ")

# Validate the email and display the result
if validate_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")
