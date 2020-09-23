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
        space_pressing_time = random.choice([00.1, 00.9, 00.9, 00.9, 00.1, 00.2, 00.9, 00.3, 00.4, 00.9, 00.5, 00.9, 00.8])

        if start_time.minute % 10 < self.random_number:
            pyautogui.press('space')
            threading.Timer(space_pressing_time, self.track).start()
        else:
            start_after_this_minutes = (10 - self.random_number) * 60
            self.wait_and_restart(start_after_this_minutes)

    def press_button(self, a, b):
        def wrapper():
            if a == 537:

                is_mouse_clicked = self.mouse_click(a, b)

                if is_mouse_clicked:
                    is_tab_changed = self.change_tab()

                if is_tab_changed:
                    print('scroll now')

                #
                # threading.Timer(1, self.track).start()

            self.mouse_click(a, b)

        return wrapper

    def start(self):
        # click git icon
        # threading.Timer(2, self.press_button(56, 818)).start()
        if self.mouse_click(56, 818):
             self.mouse_click(700, 399)

        # click git input
        # threading.Timer(5, self.press_button(537, 778)).start()

    def wait_and_restart(self, seconds):
        self.random_number = self.get_random_number()
        threading.Timer(seconds, self.press_button(537, 778)).start()

    @staticmethod
    def get_random_number():
        number_list = [7, 8, 9]
        random_number = random.choice(number_list)

        return random_number

    def mouse_click(self, x, y):
        try:
            mouse.position = (x, y)
            mouse.press(Button.left)
            mouse.release(Button.left)
            return True
        except:
            return False

    def change_tab(self):
        try:
            print(f'start in {str(datetime.now())}')
            # select random tab
            pyautogui.keyDown('ctrl')
            for i in range(0, random.randrange(1, 8)):
                pyautogui.press('tab')
            pyautogui.keyUp('ctrl')
            return True
        except:
            return False
