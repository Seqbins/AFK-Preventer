import time
import sys
from datetime import datetime, timedelta
from pynput.keyboard import Controller

keyboard = Controller()

def press_key(key_char='c'):
    """Simulate key press and release for the given key"""
    keyboard.press(key_char)
    time.sleep(0.05)
    keyboard.release(key_char)

def format_uptime(seconds):
    """Return uptime as HH:MM:SS"""
    return str(timedelta(seconds=int(seconds)))

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
    count = 0
    last_len = 0

    try:
        while True:
            press_key('c')
            count += 1

            next_press_time = datetime.now() + timedelta(seconds=interval)
            next_time_str = next_press_time.strftime("%I:%M %p")

            for remaining in range(interval, 0, -1):
                elapsed = time.time() - start_time
                uptime = format_uptime(elapsed)

                line = f"\rPress #{count:<4} | Uptime: {uptime} | Next press at {next_time_str}"
                padding = " " * max(0, last_len - len(line))
                sys.stdout.write(line + padding)
                sys.stdout.flush()
                last_len = len(line)

                time.sleep(1)

    except KeyboardInterrupt:
        print()
        print(f"Stopped by user. Total presses: {count}")
        input("Press any key to exit...")

if __name__ == "__main__":
    main()
