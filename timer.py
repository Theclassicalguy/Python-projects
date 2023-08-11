import time
import winsound

seconds = int(input("Enter the number of seconds for the timer: "))

for remaining in range(seconds, 0, -1):
    print(f"Time remaining: {remaining} seconds")
    time.sleep(1)

print("Time's up!")
winsound.Beep(1000, 1000)  # Beep sound for 1 second
