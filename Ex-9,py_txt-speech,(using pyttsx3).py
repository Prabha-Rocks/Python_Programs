import pyttsx3
def shoutout(names):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Iterate over the list of names
    for name in names:
        # Create the shoutout message
        message = f'Shoutout to {name}'
        print(message)

        # Use the engine to say the message
        engine.say(message)

    # Ensure all commands queued are spoken before the program exits
    engine.runAndWait()
if __name__ == "__main__":
    # List of names
    names = ["Riya", "Alex", "Sam", "Jordan"]

    # Call the shoutout function
    shoutout(names)
