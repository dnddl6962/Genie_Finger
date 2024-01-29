from PIL import ImageFont, ImageDraw, Image
from cvzone.HandTrackingModule import HandDetector
import cvzone
import cv2
import numpy as np
import random
import os


PATH = os.getcwd() # ./flask

font_path = f"{PATH}/static/JalnanGothicTTF.ttf"
font = ImageFont.truetype(font_path, 30)
font = ImageFont.truetype(font_path, 30)

# 이미지에 텍스트 입력 함수수
def display_text(frame, font, text):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((400, 250), text, font=font, fill=(255, 255, 0))
    frame = np.array(pil_image)
    return frame


class DragImg():
    def __init__(self, name, path, posOrigin, imgType):
        self.posOrigin = posOrigin
        self.imgType = imgType
        self.path = path
        self.name = name
        if self.imgType == 'png':
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)
        self.img = cv2.resize(self.img, dsize=(0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_LINEAR)
        self.size = self.img.shape[:2]
    def update(self, cursor):      # 커서(검지+중지) 위치벡터 업데이트 함수
        ox, oy = self.posOrigin
        h, w = self.size
        if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:

            self.posOrigin = cursor[0] - w // 2, cursor[1] - h // 2


class VideoCamera02:
    def __init__(self, listImg, done_list, orderList, plate_x, plate_y, plateImg):
        self.cap1 = cv2.VideoCapture(0)
        self.detector1 = HandDetector(detectionCon=0.7)
        self.cap1.set(3, 1280)
        self.cap1.set(4, 720)
        self.last_click_time = 0
        self.click_delay = 0.3
        self.q = 0
        self.doneItem = {}
        self.listImg트
        if done != True:
            _, buffer = cv2.imencode('.jpg', img)
            frame =  buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
        else:
            _, buffer = cv2.imencode('.jpg', img2)
            frame =  buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
