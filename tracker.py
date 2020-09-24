import threading
import pyautogui
import random
import time
from datetime import datetime
from pynput.mouse import Listener, Button, Controller

mouse = Controller()


class Tracker:
    def __init__(self):
        self.random_number = self.get_random_number()

    def track(self):
        start_time = datetime.now()

        # select random time for press space
        space_pressing_time = random.choice(
            [00.1, 00.9, 00.9, 00.9, 00.1, 00.2, 00.9, 00.3, 00.4, 00.9, 00.5, 00.9, 00.8])

        if start_time.minute % 10 < self.random_number:
            pyautogui.press('space')
            threading.Timer(space_pressing_time, self.track).start()
        else:
            start_after_this_minutes = (10 - self.random_number) * 60
            self.wait_and_restart(start_after_this_minutes)

    def press_button(self, a, b):
        if a == 537:
            time.sleep(1)
            self.change_tab()
            time.sleep(1)
            self.mouse_click(700, 450)
            time.sleep(1)
            self.random_mouse_scroll()
            time.sleep(1)
            self.mouse_click(a, b)
            time.sleep(1)
            self.track()

    def start(self):
        self.mouse_click(642, 868)
        time.sleep(1)
        pyautogui.hotkey('shift', 'esc')
        time.sleep(1)
        self.mouse_click(56, 818)
        time.sleep(1)
        self.press_button(537, 778)

    def wait_and_restart(self, seconds):
        time.sleep(seconds)
        self.random_number = self.get_random_number()
        self.press_button(537, 778)

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
        scroll_steps = random.randint(-100, 50)
        mouse.scroll(0, scroll_steps)

    @staticmethod
    def change_tab():
        print(f'start in {str(datetime.now())}')
        # select random tab
        pyautogui.keyDown('ctrl')
        for i in range(0, random.randrange(1, 8)):
            pyautogui.press('tab')
        pyautogui.keyUp('ctrl')
