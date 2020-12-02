import sys
import shelve
import psutil
import time
from pynput.mouse import Listener, Button, Controller, Events
from bcolors import bcolors


class Validator():

    def __init__(self):
        self.db = shelve.open('database')
        self.argument_value = False
        self.end = False

        if len(sys.argv) > 1:
            if sys.argv[1][:9] == '--update=':
                self.argument_value = sys.argv[1][9:] if sys.argv[1][9:] else '1'
            elif sys.argv[1][:6] == '--end=':
                self.end = sys.argv[1][6:]

                if self.end.isdigit():
                    self.end = int(self.end)
                else:
                    print('Invalid argument value')
                    exit()
            else:
                print('option is not exist')
                exit()

    @staticmethod
    def set_storm_middle_coordinates(x, y, button, pressed):
        Validator.db['storm_middle_coordinates'] = [x, y]
        return False

    def __del__(self):

        del self

    @staticmethod
    def tracker_is_running():
        its_running = False
        for proc in psutil.process_iter():
            try:
                if 'hubstaff' in proc.exe() or 'Hubstaff' in proc.exe():
                    its_running = True
            except psutil.AccessDenied:
                pass

        return its_running


class ValidateWindows(Validator):

    def __init__(self):

        super().__init__()

    def check_click_coordinates(self):

        def set_sublime_coordinates(x, y, button, pressed):
            self.db['sublime_coordinates'] = [x, y]
            return False

        def set_sublime_middle_coordinates(x, y, button, pressed):
            self.db['sublime_middle_coordinates'] = [x, y]
            return False

        def set_tracker_app_coordinates(x, y, button, pressed):
            self.db['tracker_app_coordinates'] = [x, y]
            return False

        if self.argument_value and self.argument_value not in self.db.keys():
            print('Invalid argument value')
            exit()

        if self.db.get('sublime_coordinates', False) and (False if self.argument_value == 'sublime_coordinates' else True):
            print(
                f"sublime_coordinates is a{bcolors.OKGREEN} {self.db['sublime_coordinates'][0]} and {self.db['sublime_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in Sublime Icon')
            with Listener(on_click=set_sublime_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('Sublime icon coordinates saved successfully \U0001F44D')

        if self.db.get('sublime_middle_coordinates', False) and (
        False if self.argument_value == 'sublime_middle_coordinates' else True):
            print(
                f"sublime_middle_coordinates is a{bcolors.OKGREEN} {self.db['sublime_middle_coordinates'][0]} and {self.db['sublime_middle_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in middle of Sublime')
            with Listener(on_click=set_sublime_middle_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('Sublime middle coordinates saved successfully \U0001F44D')

        if self.db.get('tracker_app_coordinates', False) and (
        False if self.argument_value == 'tracker_app_coordinates' else True):
            print(
                f"tracker_app_coordinates is a{bcolors.OKGREEN} {self.db['tracker_app_coordinates'][0]} and {self.db['tracker_app_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in Tracking app icon')
            with Listener(on_click=set_tracker_app_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('Tracking app coordinates saved successfully \U0001F44D')

        if self.db.get('sleep_command', False) and (False if self.argument_value == 'sleep_command' else True):
            print(f"sleep_command is a{bcolors.OKGREEN} {self.db['sleep_command']}{bcolors.ENDC} \U0001F44D")

        else:
            sleep_command = input('set sleep command - ')
            self.db['sleep_command'] = sleep_command.strip()

        print('Cool! \U0001F60E')
        self.db.close()
