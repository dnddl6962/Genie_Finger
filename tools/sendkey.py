import time
import pyautogui



# 키보드 입력 함수
def PressKey(hexKeyCode):
    pyautogui.keyDown(hexKeyCode)
    time.sleep(0)


def ReleaseKey(hexKeyCode):
    pyautogui.keyUp(hexKeyCode)
    time.sleep(0)
