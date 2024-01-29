import cv2
from cvzone.HandTrackingModule import HandDetector
import time
from pynput.keyboard import Controller, Key
#해당 모듈 또한 가상키보드를 이용하여
#가상 키보드와 사용자간의 상호작용을 근간으로 한다.


class HandTrackingModule:
    def __init__(self, detectionCon=0.7):
        self.detector = HandDetector(detectionCon=detectionCon)
        self.keyboard = Controller()

    def draw_buttons(self, img, buttonList):
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, button.text, (x + 20, y + 65),
                        cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 2)
        return img

    def process_frame(self, img, buttonList, last_click_time, click_delay):
        img = cv2.flip(img, 1)
        hands, img = self.detector.findHands(img, flipType=False)
        img = self.draw_buttons(img, buttonList)

        if hands:
            lmList = hands[0]['lmList']
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 2)

                    current_time = time.time()
                    if current_time - last_click_time > click_delay:
                        if button.text == "Enter":
                            self.keyboard.press(Key.enter)
                            self.keyboard.release(Key.enter)
                        elif button.text == "Delete":
                            self.keyboard.press(Key.backspace)
                            self.keyboard.release(Key.backspace)
                        else:
                            self.keyboard.type(button.text)


                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 2)
                    last_click_time = current_time

        return img, last_click_time
#해당 클래스는 HandTrackingmodule로 손을 추적하는 프레임을 생성한다.

class Button:
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = [
    Button([200, 100], "S"),  # 상단 첫 번째 버튼
    Button([400, 100], "X"),  # 상단 두 번째 버튼
    Button([600, 100], "N"),  # 상단 세 번째 버튼
    Button([800, 100], "C"),  # 상단 네 번째 버튼
    Button([1000, 100], "D"),  # 상단 다섯 번째 버튼
    Button([300, 250], "G"),
    Button([500, 250], "O"),
    Button([700, 250], "U"),
    Button([900, 250], "B"),
    Button([1000, 450], "Delete", size=[250, 100]),  # 오른쪽 아래 Delete 버튼, 고정시킨다.
    Button([45, 450], "Enter", size=[250, 100])    # 왼쪽 아래 Enter 버튼
]
#해당 버튼 클래스는 영어 알파벳을 생성할 수 있는 클래스이며

def generate_english2_frames():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    hand_tracker = HandTrackingModule(detectionCon=0.7)

    last_click_time = 0
    click_delay = 0.3

    while True:
        success, img = cap.read()
        if not success:
            break

        img, last_click_time = hand_tracker.process_frame(img, buttonList, last_click_time, click_delay)

        ret, jpeg = cv2.imencode('.jpg', img)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

    cap.release()
#위의 함수들을 접목하여 웹 캠과 가상키보드를 함께 출력할 수 있게끔
#Flask에 띄우기 위해서 적절하게 수정을 진행하였다.
