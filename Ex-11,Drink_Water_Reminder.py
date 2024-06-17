import time

while True:
    print("Time to drink water!")
    time.sleep(5)  # Sleep for 5 seconds

    response = input("Enter 'quit' to stop the reminders or else 'continue': ")
    if response.strip().lower() == 'quit':
        print("Quitting the reminder.")
        break
