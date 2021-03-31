#import keyboard
from pynput import keyboard
from pynput.mouse import Button, Controller

from threading import Thread
import time
import os
#import mouse

mouse = Controller()
start = False

def click():
    global start
    while start == True:
        #print('left-mouse pressed')
        mouse.click(Button.left)
        time.sleep(.080) # ms

def on_press(key):
    global start
    if key == keyboard.KeyCode.from_char('r'):
        if start == False:
            start = True
            Thread(target=click).start()
            print('Toggled ON')
        else:
            print('Toggled OFF')
            start = False

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()