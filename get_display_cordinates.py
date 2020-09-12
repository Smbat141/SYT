import threading
import pyautogui
import random
from pynput.mouse import Listener, Button, Controller
from tracker import Tracker

mouse = Controller()


def on_move(x, y):
    print("Mouse moved", x, y, sep="*")


def on_click(x, y, button, pressed):
    print("Mouse clicked")


def on_scroll(x, y, dx, dy):
    pass


# subprocess.call([phpstorm])
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
