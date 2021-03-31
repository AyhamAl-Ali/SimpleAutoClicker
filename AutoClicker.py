# import keyboard
# import mouse
# import os
from pynput import keyboard
from pynput.mouse import Button, Controller

from threading import Thread
import time

mouse = Controller()
start = False

speed = .080  # in ms, less values = more clicks
debug = False

toggleKey = "f6"

isDoubleClick = False


# click function
def click():
    global start
    while start == True:
        if debug is True:
            print('clicked')

        mouse.click(Button.left, 2 if isDoubleClick else 1)
        time.sleep(speed)  # ms


# On key press event
def on_press(key):
    global start
    if key == keyboard.KeyCode.from_char(toggleKey):
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
