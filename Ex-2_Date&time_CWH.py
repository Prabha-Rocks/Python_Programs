import time
from datetime import datetime

# Get the current time in HH:MM:SS format
t = time.strftime('%H:%M:%S')
print(t)

# Get the current hour
hour = int(time.strftime('%H'))
print(hour)

# Print appropriate greeting based on the current hour
if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 20:
    print("Good Evening")
elif 20 <= hour < 24:
    print("Good Night")
else:
    print("Invalid")

# Get today's date
today = datetime.today()
d = today.day
m = today.month
y = today.year
print(f"Today's date (dd/mm/yyyy): {d}/{m}/{y}")
