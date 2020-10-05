# set permissions for desktop
# xhost +
# mouse cordinates
# (56, 818)
# (537, 778)


import threading
import pyautogui
import random
import time
import pause
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller

from tracker import Tracker

x = Tracker()
x.start()
# y = 10 - (datetime.now().minute % 10)

# print(x.timestamp(), ' coming 10')
# print(datetime.now().timestamp(), ' now')
# print(int(x.timestamp()) - int(datetime.now().timestamp()))
# mouse = Controller()
# mouse.position = (588, 872)
# mouse.press(Button.left)
# mouse.release(Button.left)
#
#
# def test():
#     mouse.position = (700, 450)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     scroll_steps = random.randint(-100, 50)
#
#     mouse.scroll(0, scroll_steps)
#
#     return True
#
# x = threading.Timer(2, test).start()
# print(x)
