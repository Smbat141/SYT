# set permissions for desktop
# xhost +
# mouse cordinates
# (56, 818)
# (537, 778)


import threading
import pyautogui
import random
from pynput.mouse import Listener, Button, Controller
from tracker import Tracker

x = Tracker()
x.start()

# mouse = Controller()
# mouse.position = (588, 872)
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# #
# def test():
#     mouse.position = (700, 450)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     scroll_steps = random.randint(-100, 50)
#     print(scroll_steps)
#     mouse.scroll(0, scroll_steps)
#
#
# threading.Timer(2, test).start()
# import pandas as pd
# import os
# data_file = pd.read_csv("data.csv", encoding = "ISO-8859-1")
# print(data_file)

