import sys
import shelve
import psutil
from bcolors import bcolors


class ValidateLinux:

    def __init__(self):
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

    def check_paths(self):
        with shelve.open('database') as db:

            if self.argument_value and self.argument_value not in db.keys():
                print('Invalid argument value')
                exit()

            if db.get('storm_path', False) and (False if self.argument_value == 'storm_path' else True):
                print(f"storm_path is a{bcolors.OKGREEN} {db['storm_path']}{bcolors.ENDC} \U0001F44D")
            else:
                storm_path = input('set phpstorm starting file path (phpstorm.sh or phpstorm.bat) - ')
                db['storm_path'] = storm_path

            if db.get('storm_default_opening_file_path', False) and (
                    False if self.argument_value == 'storm_default_opening_file_path' else True):
                print(
                    f"storm_default_opening_file_path is a{bcolors.OKGREEN} {db['storm_default_opening_file_path']}{bcolors.ENDC} \U0001F44D")
            else:
                default_opening_file_path_text = "set the path to the project file you need to open every time\n" \
                                                 "for example /home/home/projects/my_project/composer.json - "

                default_opening_file_path = input(default_opening_file_path_text)
                db['storm_default_opening_file_path'] = default_opening_file_path

            if db.get('tracker_app_starting_file_path', False) and (
                    False if self.argument_value == 'tracker_app_starting_file_path' else True):
                print(
                    f"tracker_app_starting_file_path is a{bcolors.OKGREEN} {db['tracker_app_starting_file_path']}{bcolors.ENDC} \U0001F44D")
            else:
                tracker_app_starting_file_path_text = "set the path to the tracker file you need to close when finished\n" \
                                                      "for example in Linux Ubuntu " \
                                                      "/home/home/Hubstaff/HubstaffClient.bin.x86_64 - "

                tracker_app_starting_file_path = input(tracker_app_starting_file_path_text)

                db['tracker_app_starting_file_path'] = tracker_app_starting_file_path

            if db.get('sleep_command', False) and (False if self.argument_value == 'sleep_command' else True):
                print(f"sleep_command is a{bcolors.OKGREEN} {db['sleep_command']}{bcolors.ENDC} \U0001F44D")

            else:
                sleep_command = input('set sleep command - ')
                db['sleep_command'] = sleep_command

            print('Cool! \U0001F60E')

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
