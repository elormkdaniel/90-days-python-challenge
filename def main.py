def main():
    # Input: Get a list of numbers from the user
    numbers = input("Enter a list of numbers separated by spaces: ")
    
    # Convert input into a list of floats
    numbers = list(map(float, numbers.split()))
    
    # Calculate sum and average
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if len(numbers) > 0 else 0
    
    # Output results
    print(f"Sum: {total_sum}")
    print(f"Average: {average:.2f}")

if _name_ == "_main_":
    main()