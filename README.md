# AFK Preventer
A simple, lightweight Python script that keeps you from being marked AFK (Away From Keyboard) by simulating a key press every few seconds. Perfect for keeping sessions, games, or remote desktops active when you step away for a bit.

---

## Features
- Presses a key (default: `c`) automatically at your chosen interval.
- Shows live uptime and next keypress time in the console.
- Fully adjustable interval (in seconds).
- Works on Windows, macOS, and Linux.
- Lightweight and easy to stop anytime with `Ctrl + C`.

---

## Requirements
- [Python 3.8+](https://www.python.org/).
- [pynput](https://pypi.org/project/pynput/).

Install the required dependency:
```bash
pip install pynput
```

---

## Getting Started
1. Clone the repository:
```bash
git clone https://github.com/Seqbins/AFK-Preventer.git
cd AFK-Preventer
```
2. Run the script:
```bash
python AFK Preventer.py
```
3. Enter your interval:
```
Enter interval in seconds: 60
Started. Press Ctrl+C to stop.
```
The script will now press the key `c` every 60 seconds.

---

## Customization
Want to change the key that’s pressed?
Open the script and find this line:
```
press_key('c')
```
You can replace `'c'` with any key you prefer (`'space'`, `'f'`, or `'i'`).

---

## Example Output
```
Press #12 | Uptime: 00:04:22 | Next press at 03:45 PM
```

---

## Author
Created by [Seqbins](https://github.com/Seqbins).

---

## Disclaimer
This tool is provided for **educational and personal use only**.
Please do not use it to bypass AFK detection in online games or services that forbid automation.

---

## License
Released under the [MIT License](LICENSE).
