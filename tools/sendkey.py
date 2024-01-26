import time
import pyautogui



# Actuals Functions
def PressKey(hexKeyCode):
    pyautogui.keyDown(hexKeyCode)
    time.sleep(0)


def ReleaseKey(hexKeyCode):
    pyautogui.keyUp(hexKeyCode)
    time.sleep(0)

# virtual key code list
## https://msdn.microsoft.com/ko-kr/library/windows/desktop/dd375731(v=vs.85).aspx
# scancode list(ex. direct input)
## http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# def KeyPress():
#     PressKey('F') # press F
#     time.sleep(.5)
#     ReleaseKey('F') #release F

# KeyPress()