import threading
import pyautogui
import random
import time
import os
import subprocess
import shelve

from datetime import datetime, timedelta
from pynput.mouse import Button, Controller

mouse = Controller()



class Tracker:

    def __init__(self):
        self.random_number = self.get_random_number()

        with shelve.open('database') as db:
            self.storm_path = db['storm_path']
            self.default_opening_file_path = db['storm_default_opening_file_path']
            self.tracker_app_starting_file_path = db['tracker_app_starting_file_path']
            self.sleep_command = db['sleep_command']


    def track(self):
        start_time = datetime.now()

        # select random time for press space
        space_pressing_time = random.choice(
            [00.1, 00.9, 00.9, 00.9, 00.1, 00.2, 00.9, 00.3, 00.4, 00.9, 00.5, 00.9, 00.8])

        if start_time.minute % 10 < self.random_number:
            pyautogui.press('space')
            threading.Timer(space_pressing_time, self.track).start()
        else:
            minutes_left = 10 - (start_time.minute % 10)

            restart_datetime = datetime.now() + timedelta(minutes=minutes_left, seconds=0, microseconds=0)

            rounded_restart_datetime = restart_datetime - timedelta(minutes=restart_datetime.minute % 10,
                                                                    seconds=restart_datetime.second,
                                                                    microseconds=restart_datetime.microsecond)

            start_after_this_seconds = rounded_restart_datetime.timestamp() - datetime.now().timestamp()

            self.wait_and_restart(start_after_this_seconds)

    def prepare_for_track(self):
        time.sleep(1)
        self.change_tab()
        time.sleep(1)
        self.mouse_click(700, 450)
        time.sleep(1)
        self.random_mouse_scroll()
        time.sleep(1)
        self.open_git_window()
        time.sleep(1)
        self.track()

    def start(self, time_for_tracer_sleep=False):

        if time_for_tracer_sleep:
            threading.Timer(time_for_tracer_sleep * 60, self.turn_off).start()

        self.open_php_storm()
        time.sleep(1)
        self.mouse_click(700, 450)
        time.sleep(1)
        self.prepare_for_track()

    def wait_and_restart(self, seconds):
        time.sleep(seconds)
        self.random_number = self.get_random_number()
        self.start()

    def turn_off(self):
        self.open_hubstaff()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'esc')
        time.sleep(1)
        os.system(self.sleep_command)
        time.sleep(1)
        os._exit(0)

    def open_php_storm(self):
        # open project window
        subprocess.Popen([self.storm_path, self.default_opening_file_path])

    def open_hubstaff(self):
        # open project window
        subprocess.Popen([self.tracker_app_starting_file_path])


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
        for i in range(0, random.choice([8, 7, 6, 5, 7, 3, 4, 6, 8])):
            pyautogui.press('tab')
        pyautogui.keyUp('ctrl')

    @staticmethod
    def open_git_window():
        # open git window
        pyautogui.hotkey('alt', '9')
        time.sleep(1)
        # select input for typing
        pyautogui.hotkey('ctrl', 'l')

    @staticmethod
    def open_project_window():
        # open project window
        pyautogui.hotkey('alt', '1')\



