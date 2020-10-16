# set permissions for desktop
# xhost +


import threading
import pyautogui
import random
import time
import os
import sys

from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller
from multiprocessing import Pool
import subprocess
import shelve
from tracker import Tracker
from bcolors import bcolors
from validator import ValidateLinux

validate_linux = ValidateLinux()
validate_linux.check_paths()

if validate_linux.tracker_is_running():
    syt = Tracker()
    syt.start(validate_linux.end)
else:
    print(f'{bcolors.FAIL}Please make sure tracker its running{bcolors.ENDC}')


