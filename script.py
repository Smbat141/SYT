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
import os
from datetime import datetime, timedelta
from pynput.mouse import Listener, Button, Controller
from multiprocessing import Pool
from tracker import Tracker
import subprocess


x = Tracker()
x.start(70)
