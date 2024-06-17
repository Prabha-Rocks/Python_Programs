# command-line utility in Python that counts the number of words in a given text file.
import sys  # Import the sys module to access command-line arguments
def count_words(file_path='readme.txt'):
    """Prints the number of words in the specified file."""
    try:
        with open(file_path, 'r') as file:  # Open the hardcoded file in read mode
            words = file.read().split()  # Read the file and split into words
            print(f"The file '{file_path}' has {len(words)} words.")  # Print word count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")  # Error message for file not found

if __name__ == "__main__":
    count_words()  # Call the function with the hardcoded file path
