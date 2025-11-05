# AFK Preventer
A lightweight Python script that prevents AFK (Away-From-Keyboard) detection by simulating a periodic key press. Ideal for keeping sessions, games, or remote connections active while idle.

---

## Features
- Automatically presses a key (default: `c`) at a set interval.
- Displays live countdown and uptime in the console.
- Adjustable interval (in seconds).
- Simple, cross-platform (Windows, MacOS, Linux), and dependency-light.
- Easily stopped using `Ctrl + C`.

---

## Requirements
- [python](https://www.python.org/) 3.8 or newer.
- [pynput](https://pypi.org/project/pynput/) library.

Install with:
```bash
pip install pynput
```

---

## Usage
1. Clone the repository:
```bash
git clone https://github.com/Seqbins/AFK-Preventer.git
cd AFK-Preventer
```
2. Run the script:
```bash
python AFK Preventer.py
```
3. Enter your desired interval (in seconds).
Example:
```
Enter interval in seconds: 60
Started. Press Ctrl+C to stop.
```
4. The script will automatically press the key `c` every 60 seconds.

---

## Customization
You can modify the default key by editing this line inside the script:
```
press_key('c')
```
Change 'c' to any key you prefer (e.g., 'space', 'shift', 'f', etc.).

---

## Example Output
```
Next key press in: 45 seconds | Uptime: 00:03:25
```

---

## Author
Created by [Seqbins](https://github.com/Seqbins).

---

## Disclaimer
This tool is provided for **educational and personal use only**.
Do not use it to bypass AFK detection in online games or platforms that prohibit automation.

---

## License
This project is licensed under the [MIT License](LICENSE) - you’re free to use, modify, and distribute it as long as proper credit is given.
