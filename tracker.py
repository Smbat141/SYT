import random
import time
import os
import sys

import threading
import pyautogui
import subprocess
import shelve
import psutil

from datetime import datetime, timedelta
from pynput.mouse import Button, Controller

mouse = Controller()
pyautogui.FAILSAFE = False


class Tracker:

    def __init__(self):
        self.random_number = self.get_random_number()

        with shelve.open('database') as db:

            self.storm_middle_coordinates = db['storm_middle_coordinates']
            self.sleep_command = db['sleep_command']

            if sys.platform == 'linux':
                self.storm_path = db['storm_path']
                self.default_opening_file_path = db['storm_default_opening_file_path']
                self.tracker_app_starting_file_path = db['tracker_app_starting_file_path']
            else:
                self.storm_coordinates = db['storm_coordinates']
                self.tracker_app_coordinates = db['tracker_app_coordinates']

    def track(self):
        start_time = datetime.now()

        # select random time for press space
        space_pressing_time = random.choice(
            [00.1, 00.9, 00.9, 00.9, 00.1, 00.2, 00.9, 00.3, 00.4, 00.9, 00.5, 00.9, 00.8])

        operations = ['click', 'space']

        operation = random.choice(operations)

        if start_time.minute % 10 < self.random_number:
            self.open_git_window()
            if operation == 'space':
                pyautogui.press('space')
            else:
                self.mouse_click(*self.storm_middle_coordinates)

            threading.Timer(space_pressing_time, self.track).start()
        else:
            minutes_left = 10 - (start_time.minute % 10)

            restart_datetime = datetime.now() + timedelta(minutes=minutes_left, seconds=0, microseconds=0)

            rounded_restart_datetime = restart_datetime - timedelta(minutes=restart_datetime.minute % 10,
                                                                    seconds=restart_datetime.second,
                                                                    microseconds=restart_datetime.microsecond)

            start_after_this_seconds = rounded_restart_datetime.timestamp() - datetime.now().timestamp()

            threading.Timer(start_after_this_seconds, self.wait_and_restart).start()

    def prepare_for_track(self):
        time.sleep(2)
        self.change_tab()
        time.sleep(2)
        self.mouse_click(*self.storm_middle_coordinates)
        time.sleep(2)
        self.random_mouse_scroll()
        time.sleep(2)
        self.open_git_window()
        time.sleep(1)
        self.track()

    def start(self, time_for_tracker_sleep=False):

        if time_for_tracker_sleep:
            threading.Timer(time_for_tracker_sleep * 60, self.turn_off).start()

        self.open_php_storm()
        time.sleep(3)
        self.prepare_for_track()

    def wait_and_restart(self):
        self.random_number = self.get_random_number()
        if sys.platform == 'linux':
            self.start()
        else:
            self.prepare_for_track()

    def turn_off(self):
        self.kill_tracker_process()
        time.sleep(1)
        os.system(self.sleep_command)
        time.sleep(1)
        os._exit(0)

    def open_php_storm(self):
        # open project window
        if sys.platform == 'linux':
            subprocess.Popen([self.storm_path, self.default_opening_file_path])
        else:
            self.mouse_click(*self.storm_coordinates)
    
    @staticmethod
    def kill_tracker_process():
        # find and kill process
        its_running = False
        for proc in psutil.process_iter():
            try:
                if 'hubstaff' in proc.exe() or 'Hubstaff' in proc.exe():
                    proc.kill()
                    its_running = True
            except psutil.AccessDenied:
                pass
        if not its_running:
            os.system("systemctl poweroff")

    def open_git_window(self):
        self.mouse_click(*self.storm_middle_coordinates)
        time.sleep(1)
        # open git window
        pyautogui.hotkey('alt', '9')
        time.sleep(1)
        # select input for typing
        pyautogui.hotkey('ctrl', 'l')

    @staticmethod
    def get_random_number():
        number_list = [6, 7, 8]
        random_number = random.choice(number_list)

        return random_number

    @staticmethod
    def mouse_click(x, y):
        mouse.position = (x, y)
        mouse.press(Button.left)
        mouse.release(Button.left)

    @staticmethod
    def random_mouse_scroll():
        scroll_steps = random.randint(-70, 70)
        mouse.scroll(0, scroll_steps)

    @staticmethod
    def change_tab():
        print(f'start in {str(datetime.now())}')
        # select random tab
        pyautogui.keyDown('ctrl')
        pyautogui.press('tab')
        for i in range(0, random.randint(1, 20)):
            pyautogui.press('down')
        pyautogui.keyUp('ctrl')


    @staticmethod
    def open_project_window():
        # open project window
        pyautogui.hotkey('alt', '1')
