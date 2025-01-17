import json

# Function to read and process the JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return None

# Function to retrieve specific values based on user input
def get_value_from_json(data):
    while True:
        key = input("Enter the key to retrieve its value (or type 'exit' to quit): ")
        if key.lower() == 'exit':
            print("Exiting the program.")
            break
        elif key in data:
            print(f"The value for '{key}' is: {data[key]}")
        else:
            print(f"Key '{key}' not found in the JSON file.")

# Main script
file_path = input("Enter the path to the JSON file: ")
data = read_json(file_path)

if data:
    print("JSON data loaded successfully!")
    get_value_from_json(data)
