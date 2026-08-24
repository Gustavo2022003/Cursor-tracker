# 🖱️ Mouse Distance Tracker

A tiny project made just for fun to find out how many meters the mouse cursor travels across the screen throughout the day. Nothing too serious — pure curiosity!

## What it does

Runs quietly in the system tray and shows, in real time, the total distance traveled by the mouse via a small overlay in the corner of the screen, converted from pixels to meters.

## How it works

- Continuously tracks the cursor position and calculates the Euclidean distance between each movement
- Converts pixels to meters using the screen's DPI (96 DPI as default)
- Displays the result in a floating overlay always on top
- Tray icon with an option to quit

## Tech stack

- Python
- [`pyautogui`](https://pypi.org/project/PyAutoGUI/) — mouse position tracking
- [`numpy`](https://pypi.org/project/numpy/) — distance calculation
- `tkinter` — screen overlay (built into Python)
- [`pystray`](https://pypi.org/project/pystray/) — system tray icon
- [`Pillow`](https://pypi.org/project/Pillow/) — tray icon image generation

## Installation

Clone the repo:

```bash
git clone https://github.com/your-username/mouse-distance-tracker.git
cd mouse-distance-tracker
```

(Optional but recommended) create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Install the dependencies:

Go inside the `main.py` directory and execute:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

- A small overlay will appear in the top-right corner of the screen, showing the distance traveled in meters.
- A tray icon will also appear in the system tray.
- To quit, **right-click the tray icon** and select **"Exit"**.

## Building a standalone executable (Windows)

If you want a `.exe` that runs without needing Python installed:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name "MouseTracker" main.py
```

The executable will be generated inside the `dist/` folder.

## Notes

- The pixel-to-meter conversion assumes a fixed 96 DPI, which is a common default but may not match every monitor/scaling setup exactly.
- This was built as a weekend project to practice Python — no big ambitions, just a fun way to visualize something that's normally invisible: how far your mouse actually travels.

## License

Feel free to use, modify, and share this project however you'd like.
