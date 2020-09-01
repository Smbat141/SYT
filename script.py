# set permissions for desktop
# xhost +
# mouse cordinates
# (56, 818)
# (537, 778)

# phpstorm = '/home/home/.local/bin/phpstorm'

# def on_move(x, y):
#     print ("Mouse moved",x, y, sep="*")
#
# def on_click(x, y, button, pressed):
#     print ("Mouse clicked")
#
# def on_scroll(x, y, dx, dy):
#     print ("Mouse scrolled")
#
# #subprocess.call([phpstorm])
# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
# 	listener.join()

from tracker import Tracker

x = Tracker()
x.start()

# import threading
# import pyautogui
# import random
#
# from pynput.mouse import Listener, Button, Controller
#
#
# mouse = Controller()
#
# mouse.position = (537, 778)
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# def test():
#     pyautogui.keyDown('ctrl')
#
#     for i in range(0,random.randrange(1, 8)):
#         pyautogui.press('tab')
#
#     pyautogui.keyUp('ctrl')
#
# threading.Timer(2, test).start()

