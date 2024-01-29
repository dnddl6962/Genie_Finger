import time
import pyautogui



# Actuals Functions
def PressKey(hexKeyCode):
    pyautogui.keyDown(hexKeyCode)
    time.sleep(0)


def ReleaseKey(hexKeyCode):
    pyautogui.keyUp(hexKeyCode)
    time.sleep(0)
