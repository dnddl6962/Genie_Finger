import tools.sendkey as sendkey
from PIL import ImageFont, ImageDraw, Image
from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np
import os

PATH = os.getcwd()  # ./flask

font_path = f"{PATH}/static/JalnanGothicTTF.ttf"

def display_text(pil_img, hand_direction):
    font = ImageFont.truetype(font_path, 40)
    pil_image = Image.fromarray(pil_img)
    draw = ImageDraw.Draw(pil_image)
    if hand_direction == '왼쪽' or hand_direction == '아래':
        draw.text((430, 440), f"{hand_direction}", font=font, fill=(255, 255, 0))
    elif hand_direction == '오른쪽' or hand_direction == '위':
        draw.text((860, 440), f"{hand_direction}", font=font, fill=(255, 255, 0))
    img = np.array(pil_image)
    return img

def generate_maze_frames():
    detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
    current_key_pressed = set()
    cap = cv2.VideoCapture(0)

    while True:
        
        success, img = cap.read()
        keyPressed = False
        spacePressed=False
        key_count=0
        key_pressed=0
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)


        if hands and len(hands) == 2:
            
            if hands[0]['type'] == 'Left' or hands[1]['type'] == 'Right':

                hand1 = hands[1]  # 오른손
                fingerUp1=detector.fingersUp(hand1)
                hand2 = hands[0]  # 왼손
                fingerUp2=detector.fingersUp(hand2)
                handType1 = hand1["type"]
                handType2 = hand2["type"]

            elif hands[1]['type'] == 'Left' or hands[0]['type'] == 'Right':

                hand1 = hands[0]  # 오른손
                fingerUp1=detector.fingersUp(hand1)
                hand2 = hands[1]  # 왼손
                fingerUp2=detector.fingersUp(hand2)
                handType1 = hand1["type"]
                handType2 = hand2["type"]

            # 오른손을 먼저 인식 시켜야 됨

            if fingerUp1==[1,1,1,0,0] and handType1 == 'Right':
                # cv2.putText(img, 'Up', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                # hexKeyCode = 0x11
                img = display_text(img, "위")
                hexKeyCode = 'w'
                sendkey.PressKey(hexKeyCode)
            
                spacePressed=True
                current_key_pressed.add(hexKeyCode)
                key_pressed = hexKeyCode
                keyPressed = True
                key_count=key_count+1

            if fingerUp2==[1,1,1,0,0] and handType2 == 'Left':
                # cv2.putText(img, 'Down', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                # hexKeyCode = 0x1F
                img = display_text(img, "아래")
                hexKeyCode = 's'
                sendkey.PressKey(hexKeyCode)
            
                spacePressed=True
                current_key_pressed.add(hexKeyCode)
                key_pressed = hexKeyCode
                keyPressed = True
                key_count=key_count+1

            if fingerUp1==[1,1,0,0,0] and handType1 == 'Right':
                # cv2.putText(img, 'Right', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                # hexKeyCode = 0x20
                img = display_text(img, "오른쪽")
                hexKeyCode = 'd'
                sendkey.PressKey(hexKeyCode)
            
                spacePressed=True
                current_key_pressed.add(hexKeyCode)
                key_pressed = hexKeyCode
                keyPressed = True
                key_count=key_count+1

            if fingerUp2==[1,1,0,0,0] and handType2 == 'Left':
                # cv2.putText(img, 'Left', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
                # hexKeyCode = 0x1E
                img = display_text(img, "왼쪽")
                hexKeyCode = 'a'
                sendkey.PressKey(hexKeyCode)
            
                spacePressed=True
                current_key_pressed.add(hexKeyCode)
                key_pressed = hexKeyCode
                keyPressed = True
                key_count=key_count+1

            if not keyPressed and len(current_key_pressed) != 0:
                for key in current_key_pressed:
                    sendkey.ReleaseKey(key)
                
                current_key_pressed = set()
            elif key_count==1 and len(current_key_pressed)==2:    
                for key in current_key_pressed:             
                    if key_pressed!=key:
                        sendkey.ReleaseKey(key)
                    
                current_key_pressed = set()
                for key in current_key_pressed:
                    sendkey.ReleaseKey(key)
                
                current_key_pressed = set()

        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg; charset=utf-8\r\n\r\n' + frame + b'\r\n')

    cap.release()

