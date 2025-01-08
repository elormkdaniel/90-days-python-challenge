# Age checker program

# Ask the user for their age
age = int(input("Enter your age: "))

# Check eligibility for services
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are too young to vote.")

# Additional checks for other services
if age >= 16:
    print("You are eligible to apply for a driver's license.")
else:
    print("You are too young to apply for a driver's license.")

if age >= 21:
    print("You are eligible to purchase alcohol in some countries.")
else:
    print("You are too young to purchase alcohol.")
