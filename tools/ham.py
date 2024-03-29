from PIL import ImageFont, ImageDraw, Image
from cvzone.HandTrackingModule import HandDetector
import cvzone
import cv2
import numpy as np
import random
import os



PATH = os.getcwd()  # ./flask

font_path = f"{PATH}/static/JalnanGothicTTF.ttf"
font = ImageFont.truetype(font_path, 30)

# 이미지에 텍스트 입력 함수
def display_text(frame, font, text, fill):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((400, 250), text, font=font, fill=fill)
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
    def update(self, cursor):                   # 커서(검지+중지) 위치벡터 업데이트 함수
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
        self.listImg = listImg
        self.done_list = done_list
        self.orderList = orderList
        self.plate_x = plate_x
        self.plate_y = plate_y
        self.plateImg = plateImg
        self.done = False
    def __del__(self):
        self.cap1.release()
    def get_frame02(self, img):
        img = cv2.flip(img, 1)
        hands, img = self.detector1.findHands(img, flipType=False)
        y = 0
        if hands:
            lmList = hands[0]['lmList']
            length, info, img = self.detector1.findDistance((lmList[4][0], lmList[4][1]), (lmList[8][0], lmList[8][1]), img)   # 검지와 중지 사이 거리 계산해서 그랩 기능 구현
            if length < 70:
                cursor = lmList[8]
                for idx, imgObject in enumerate(self.listImg):
                    if imgObject not in self.done_list:
                        imgObject.update(cursor)
                        self.listImg[idx], self.listImg[-1] = self.listImg[-1], self.listImg[idx]
                        if 360 < imgObject.posOrigin[0] < 800 and 400 < imgObject.posOrigin[1] < 500 and imgObject.name not in self.orderList:  
                            self.doneItem[imgObject] = self.plate_y - self.q                # 재료를 접시 범위 내에 드래그한다면 재료 위치벡터를 접시 위로 고정
                            self.orderList.append(imgObject.name)                           # 재료를 놓은 순서대로 리스트에 append
                            self.done_list.append(list(self.doneItem.keys())[-1])
                            self.q += 20
                    else:
                        self.listImg[idx], self.listImg[y] = self.listImg[y], self.listImg[idx]
                        y += 1
        try:
            for imgObject in self.listImg:    # 재료 이미지들의 위치벡터를 출력 이미지에 오버레이
                h, w = imgObject.size
                ox, oy = imgObject.posOrigin
                if imgObject.imgType == "png" and imgObject not in self.done_list:
                    img = cvzone.overlayPNG(img, imgObject.img, [ox, oy])
                else:
                    if imgObject == self.plateImg:
                        img = cvzone.overlayPNG(img, imgObject.img, [400, 400])
                    else:
                        if imgObject in list(self.doneItem.keys()):
                            img = cvzone.overlayPNG(img, imgObject.img, [self.plate_x, self.doneItem[imgObject]])
                        else:
                            img = cvzone.overlayPNG(img, imgObject.img, [self.plate_x, self.plate_y])
        except:
            pass

        # 정답 레시피 리스트 길이만큼 재료를 놓았다면 루프 종료
        correct_list = ['breaddown.png', 'vege.png', 'tomato.png', 'peacle.png', 'meat.png', 'cheese.png', 'breadup.png']
        if len(self.orderList) == len(correct_list):
            self.done = True
        return img, self.done, self.cap1
    

def drawImage(randomList, path):            # 맨처음 재료 및 접시 이미지 배치
    done_list = []
    listImg = []
    y = 0
    for x, pathImg in enumerate(randomList):
        if 'png' in pathImg:
            imgType = 'png'
        else:
            imgType = 'jpg'
        if 'plate' in pathImg:
            plateImg = DragImg(pathImg, f'{path}/{pathImg}', [400, 400], imgType)
            listImg.append(plateImg)
            done_list.append(plateImg)
            y = -1
            continue
        else:
            listImg.append(DragImg(pathImg, f'{path}/{pathImg}', [30 + (x + y) * 150, 150], imgType))
    return (listImg, done_list, plateImg)



def generate_burger_frames():


    path = f"{PATH}/tools/ham_image"
    myList = os.listdir(path)
    listImg = []
    done_list = []
    orderList = []
    plate_x, plate_y = 550, 480
    y = 0
    randomList = random.sample(myList, len(myList))
    listImg, done_list, plateImg = drawImage(randomList, path)
    camera = VideoCamera02(listImg, done_list, orderList, plate_x, plate_y, plateImg)

    while True:
        success, img = camera.cap1.read()
        if not success:
            break
        get_frame = camera.get_frame02(img)
        img = get_frame[0]
        done = get_frame[1]
        cap1 = get_frame[2]
        dx, dy = 400, 250
        correct_list = ['breaddown.png', 'vege.png', 'tomato.png', 'peacle.png', 'meat.png', 'cheese.png', 'breadup.png']

        # 재료 순서 리스트 바탕으로 정답 및 오답 출력
        if done == True:
            if camera.orderList == correct_list:
                img2= display_text(img, font, '축하해요. 레시피대로 맛있는 햄버거를 만들었어요!', fill=(0, 255, 0))

            elif camera.orderList != correct_list and len(camera.orderList) == len(correct_list):
                img2 = display_text(img, font, "아쉬워요. 레시피대로는 아니지만 괜찮은 햄버거네요", fill=(0, 127, 255))

        # 재료가 다 놓이기 전까지 업데이트 되는 이미지 화면에 출력
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