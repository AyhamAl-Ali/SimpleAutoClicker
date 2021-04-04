# import keyboard
# import mouse
# import os

from pynput import keyboard
from pynput.mouse import Button, Controller

from threading import Thread
import time


# Variables
speed = .080  # in ms, less values = more clicks

isToggleKeyAChar = True  # if toggle key is any character such as 'r' or 'q' set this to True otherwise if toggleKey is like F6 then set it to False
toggleKey = "r"

clickType = Button.left  # Button.left, Button.right, Button.middle
isDoubleClick = False

# send debug message?
debug = False


# define mouse
mouse = Controller()
# Don't edit this - toggle script
start = False


# click function
def click():
    global start
    while start:
        if debug is True:
            print('clicked')

        mouse.click(clickType, 2 if isDoubleClick else 1)
        time.sleep(speed)  # ms


# On key press event
def on_press(key):
    global start
    if isToggleKeyAChar:
        if key != keyboard.KeyCode.from_char(toggleKey):
            return
    else:
        if key != keyboard.Key.f6:
            return

    if not start:
        start = True
        Thread(target=click).start()  # start in another thread so it doesn't hold this code
        print('Toggled ON')
    else:
        print('Toggled OFF')
        start = False


# Listener register
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # join listener to this
