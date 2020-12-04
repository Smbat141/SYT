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


class ValidateLinux(Validator):

    def __init__(self):
        super().__init__()

    def check_paths(self):
        if self.argument_value and self.argument_value not in self.db.keys():
            print('Invalid argument value')
            exit()

        if self.db.get('app_name', False) and (False if self.argument_value == 'app_name' else True):
            print(f"app_name is a{bcolors.OKGREEN} {self.db['app_name']}{bcolors.ENDC} \U0001F44D")
        else:
            app_name = input('set app name (phpstorm or sublime_text)-')
            self.db['app_name'] = app_name.strip()

        if self.db.get('tracker_app_starting_file_path', False) and (
                False if self.argument_value == 'tracker_app_starting_file_path' else True):
            print(
                f"tracker_app_starting_file_path is a{bcolors.OKGREEN} {self.db['tracker_app_starting_file_path']}{bcolors.ENDC} \U0001F44D")
        else:
            tracker_app_starting_file_path_text = "set the path to the tracker file you need to close when finished\n" \
                                                  "for example in Linux Ubuntu " \
                                                  "/home/home/Hubstaff/HubstaffClient.bin.x86_64 - "

            tracker_app_starting_file_path = input(tracker_app_starting_file_path_text)

            self.db['tracker_app_starting_file_path'] = tracker_app_starting_file_path.strip()

        if self.db.get('storm_middle_coordinates', False) and (
        False if self.argument_value == 'storm_middle_coordinates' else True):
            print(
                f"storm_middle_coordinates is a{bcolors.OKGREEN} {self.db['storm_middle_coordinates'][0]} and {self.db['storm_middle_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in middle of PhpStorm')
            with Listener(on_click=self.set_storm_middle_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('PhpStorm middle coordinates saved successfully \U0001F44D')

        if self.db.get('sleep_command', False) and (False if self.argument_value == 'sleep_command' else True):
            print(f"sleep_command is a{bcolors.OKGREEN} {self.db['sleep_command']}{bcolors.ENDC} \U0001F44D")

        else:
            sleep_command = input('set sleep command - ')
            self.db['sleep_command'] = sleep_command.strip()

        print('Cool! \U0001F60E')
        self.db.close()


class ValidateWindows(Validator):

    def __init__(self):
        super().__init__()

    def check_click_coordinates(self):

        def set_storm_coordinates(x, y, button, pressed):
            self.db['storm_coordinates'] = [x, y]
            return False

        def set_storm_middle_coordinates(x, y, button, pressed):
            self.db['storm_middle_coordinates'] = [x, y]
            return False

        def set_tracker_app_coordinates(x, y, button, pressed):
            self.db['tracker_app_coordinates'] = [x, y]
            return False

        if self.argument_value and self.argument_value not in self.db.keys():
            print('Invalid argument value')
            exit()

        if self.db.get('storm_coordinates', False) and (False if self.argument_value == 'storm_coordinates' else True):
            print(
                f"storm_coordinates is a{bcolors.OKGREEN} {self.db['storm_coordinates'][0]} and {self.db['storm_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in PhpStorm Icon')
            with Listener(on_click=set_storm_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('PhpStorm icon coordinates saved successfully \U0001F44D')

        if self.db.get('storm_middle_coordinates', False) and (
        False if self.argument_value == 'storm_middle_coordinates' else True):
            print(
                f"storm_middle_coordinates is a{bcolors.OKGREEN} {self.db['storm_middle_coordinates'][0]} and {self.db['storm_middle_coordinates'][1]}{bcolors.ENDC} \U0001F44D")
        else:
            print('Please click in middle of PhpStorm')
            with Listener(on_click=set_storm_middle_coordinates) as listener:
                listener.join()
                time.sleep(1)
            print('PhpStorm middle coordinates saved successfully \U0001F44D')

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
            self.db['sleep_command'] = sleep_command

        print('Cool! \U0001F60E')
        self.db.close()
