# set permissions for desktop
# xhost +


import threading
import pyautogui
import random
import time
import os
import sys
import psutil

from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller
from multiprocessing import Pool
import subprocess
import shelve

mouse = Controller()
mouse.position = (950, 1046)
mouse.press(Button.left)
mouse.release(Button.left)

# 306,135
# 1609, 133
# 1609, 1010
time.sleep(1)


mouse = Controller()
mouse.position = (303, 135)
mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(1)

pyautogui.keyDown('winleft')
pyautogui.press('prtscr')
pyautogui.keyUp('winleft')

time.sleep(1)
mouse = Controller()
mouse.position = (303, 135)
mouse.press(Button.left)

time.sleep(1)

mouse.position = (1607, 135)

time.sleep(1)

mouse.position = (1607, 1010)
mouse.release(Button.left)



