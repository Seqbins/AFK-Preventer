import time
import sys
from datetime import timedelta
from pynput.keyboard import Controller

keyboard = Controller()

def press_key(key_char='c'):
    """Simulate key press and release for the given key"""
    keyboard.press(key_char)
    time.sleep(0.05)
    keyboard.release(key_char)

def main():
    try:
        interval = int(input("Enter interval in seconds: "))
        if interval <= 0:
            raise ValueError
    except ValueError:
        print("Invalid interval. Aborting...")
        sys.exit(1)

    print("Started. Press Ctrl+C to stop.")
    start_time = time.time()

    try:
        while True:
            press_key('c')
            for i in range(interval, 0, -1):
                elapsed = int(time.time() - start_time)
                uptime = str(timedelta(seconds=elapsed))
                if len(uptime.split(":")) == 2:
                    uptime = "00:" + uptime
                sys.stdout.write(
                    f"\rNext key press in: {i} seconds | Uptime: {uptime}    "
                )
                sys.stdout.flush()
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
