import random
import string

def add_random_chars(word, n=3):
    # Generate random characters
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
    # Append random characters to the start and end of the word
    return random_chars + word + random_chars

def code_word(word):
    if len(word) >= 3:
        # Move the first letter to the end and add random characters
        word = word[1:] + word[0]
        return add_random_chars(word)
    else:
        # Reverse the word if it's less than 3 characters
        return word[::-1]

def decode_word(word):
    if len(word) < 3:
        # Reverse the word if it's less than 3 characters
        return word[::-1]
    else:
        # Remove 3 characters from start and end, move last letter to the start
        word = word[3:-3]
        return word[-1] + word[:-1]

def process_message(message, mode):
    words = message.split()
    if mode == 'code':
        # Encode each word
        return ' '.join(code_word(word) for word in words)
    elif mode == 'decode':
        # Decode each word
        return ' '.join(decode_word(word) for word in words)
    else:
        raise ValueError("Invalid mode. Choose 'code' or 'decode'.")

# Ask user whether to code or decode
mode = input("Do you want to code or decode? ").strip().lower()
# Input the message
message = input("Enter the message: ").strip()
# Process the message based on the chosen mode
result = process_message(message, mode)
# Print the result
print(f"Result: {result}")
