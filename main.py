import pyautogui as pg
import numpy as np
import tkinter as tk
import threading
import pystray
from PIL import Image, ImageDraw

distance_px = 0
root = None
icon = None
DPI = 96 # Adjust your DPI here


def euclidean_distance(a, b):
    cat_1 = a.x - b.x
    cat_2 = a.y - b.y
    return np.hypot(cat_1, cat_2)


def px_to_m(px):
    return (px / DPI) * 0.0254


def track_mouse(label):
    global distance_px
    prev_pos = pg.position()

    while True:
        current_pos = pg.position()

        if current_pos != prev_pos:
            distance_px += euclidean_distance(prev_pos, current_pos)
            prev_pos = current_pos

            meters = px_to_m(distance_px)
            label.config(text=f"{meters:.2f} m")


def create_tray_image():
    imagem = Image.new('RGB', (64, 64), color=(0, 128, 255))
    dc = ImageDraw.Draw(imagem)
    dc.text((20, 20), "D", fill=(255, 255, 255))
    return imagem


def close(icon_ref, item):
    icon_ref.stop()
    root.destroy()


def setup_tray():
    global icon
    menu = pystray.Menu(
        pystray.MenuItem("Sair", close)
    )
    icon = pystray.Icon("mouse_tracker", create_tray_image(), "Mouse Tracker", menu)
    icon.run()


def main():
    global root

    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.attributes('-alpha', 0.85)
    root.configure(bg='black')

    screen_w = root.winfo_screenwidth()
    root.geometry(f"150x40+{screen_w - 160}+10")

    label = tk.Label(root, text="0.00 m", fg="white", bg="black", font=("Consolas", 14))
    label.pack(expand=True, fill="both")

    threading.Thread(target=track_mouse, args=(label,), daemon=True).start()

    threading.Thread(target=setup_tray, daemon=True).start()

    root.mainloop()


if __name__ == "__main__":
    main()
