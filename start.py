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
from tracker import Tracker
from bcolors import bcolors
from validator import ValidateLinux, ValidateWindows


if sys.platform == 'linux':
    validator = ValidateLinux()
    validator.check_paths()
else:
    validator = ValidateWindows()
    validator.check_click_coordinates()

if validator.tracker_is_running():
    syt = Tracker()
    syt.start(validator.end)
else:
    print(f'{bcolors.FAIL}Please make sure tracker its running{bcolors.ENDC}')


# mouse = Controller()
# mouse.position = (800, 600)
# mouse.press(Button.left)
# mouse.release(Button.left)
# time.sleep(1)
# print(f'start in {str(datetime.now())}')
# # select random tab
# pyautogui.keyDown('ctrl')
# pyautogui.press('tab')
# for i in range(0, random.randint(1, 20)):
#     pyautogui.press('down')
# pyautogui.keyUp('ctrl')

