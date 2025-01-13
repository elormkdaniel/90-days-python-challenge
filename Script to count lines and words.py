# Script to count lines and words in a text file

# Function to count lines and words
def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            
            print(f"The file '{file_path}' has:")
            print(f"- {line_count} line(s)")
            print(f"- {word_count} word(s)")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask the user for the file path
file_path = input("Enter the path to the text file: ")

# Call the function
count_lines_and_words(file_path)
