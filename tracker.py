import threading
import pyautogui
import random
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
            [0.1, 1, 0.9, 1.3, 0.9, 0.9, 0.1, 0.2, 0.9, 0.3, 0.4, 0.9, 0.5, 0.9, 0.8, 1.3])

        if start_time.minute % 10 < self.random_number:
            pyautogui.press('space')
            threading.Timer(space_pressing_time, self.track).start()
        else:
            start_after_this_minutes = (10 - self.random_number) * 60
            self.wait_and_restart(start_after_this_minutes)

    def press_button(self, a, b):
        def wrapper():
            if a == 537:
                mouse.position = (a, b)
                mouse.press(Button.left)
                mouse.release(Button.left)

                print(f'start in {str(datetime.now())}')
                # select random tab
                pyautogui.keyDown('ctrl')
                for i in range(0, random.randrange(1, 8)):
                    pyautogui.press('tab')
                pyautogui.keyUp('ctrl')

                threading.Timer(1, self.track).start()

            mouse.position = (a, b)
            mouse.press(Button.left)
            mouse.release(Button.left)

        return wrapper

    def start(self):
        # click git icon
        threading.Timer(2, self.press_button(56, 818)).start()

        # click git input
        threading.Timer(5, self.press_button(537, 778)).start()

    def wait_and_restart(self, seconds):
        self.random_number = self.get_random_number()
        threading.Timer(seconds, self.press_button(537, 778)).start()

    @staticmethod
    def get_random_number():
        number_list = [7, 6, 8, 7, 6, 8, 7, 6, 8, 7, 6, 8]
        random_number = random.choice(number_list)

        return random_number
