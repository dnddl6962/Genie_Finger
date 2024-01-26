import cv2
from cvzone.HandTrackingModule import HandDetector
import time
from pynput.keyboard import Controller, Key



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


class Button:
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = [
    Button([200, 200], "A"),
    Button([400, 200], "R"),
    Button([600, 200], "T"),
    Button([800, 200], "C"),
    Button([1000, 200], "S"),
    Button([1000, 400], "Delete", size=[250, 100]),
    Button([45, 400], "Enter", size=[250, 100])
]


def generate_english_frames():
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
