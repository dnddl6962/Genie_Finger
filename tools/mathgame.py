from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import random
import time
import mediapipe as mp
import os
# hands 객체를 전역으로 선언
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1
)
PATH = os.getcwd()  # ./flask

font_path = f"{PATH}/static/JalnanGothicTTF.ttf"
font = ImageFont.truetype(font_path, 30)

width, height = 640, 480
number_coordinates_upper = [(width // 10 * i + width // 7, height // 4) for i in range(1, 11)]
number_coordinates_lower = [(width // 10 * (i - 10) + width // 7, 3 * height // 4) for i in range(11, 21)]
number_coordinates_upper = [(coord[0] - 150, coord[1]) for coord in number_coordinates_upper]
number_coordinates_lower = [(coord[0] - 150, coord[1]) for coord in number_coordinates_lower]
def generate_problem():
    num1 = random.randint(2, 10)
    if num1 > 1:
        num2 = random.randint(1, num1-1)
    operation = random.choice(["+", "-"])
    if operation == "+":
        return num1, num2, num1 + num2, "+"
    else:
        return num1, num2, num1 - num2, "-"
def initialize_hands():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=1
    )
    return hands
def check_answer(selected_number, correct_answer, operation):
    return selected_number == str(correct_answer)
def landmarks_to_pixel(landmark, frame_width, frame_height):
    x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)
    return x, y
def display_problem(frame, problem_text):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((20, 50), problem_text, font=font, fill=(0, 0, 0))
    frame = np.array(pil_image)
    return frame
def display_numbers(frame):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    for i, (number_x, number_y) in enumerate(number_coordinates_upper):
        draw.text((number_x, number_y), str(i + 1), font=font, fill=(0, 0, 0))
    for i, (number_x, number_y) in enumerate(number_coordinates_lower):
        draw.text((number_x, number_y), str(i + 11), font=font, fill=(0, 0, 0))
    frame = np.array(pil_image)
    return frame
def display_user_answer(frame, user_answer):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((width // 2 - 50, height // 2 + 50), f"지금 고른 숫자: {user_answer}", font=font, fill=(0, 0, 0))
    frame = np.array(pil_image)
    return frame
def display_result(frame, result_message, color):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((width // 2 - 50, height // 2), result_message, font=font, fill=color)
    frame = np.array(pil_image)
    return frame
def display_end(frame):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    draw.text((200, height // 2 - 50), "모든 문제를 맞췄어요!", font=font, fill=(0, 0, 255))
    frame = np.array(pil_image)
    return frame
def generate_frames(hands):
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    current_problem = generate_problem()
    correct_answer = str(current_problem[2])
    user_answer = ""
    num_correct = 0
    num_questions = 10
    correct_display_time = 1.0
    wrong_display_time = 1.0
    end_display_time = None
    all_correct_message_displayed = False
    while num_correct < num_questions:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            index_tip = landmarks[8]
            index_x, index_y = landmarks_to_pixel(index_tip, width, height)
            cv2.circle(frame, (index_x, index_y), 20, (0, 255, 0), -1)
            for i, (number_x, number_y) in enumerate(number_coordinates_upper + number_coordinates_lower):
                if abs(index_x - number_x) < 20 and abs(index_y - number_y) < 20:
                    user_answer = str(i + 1)
                    break
            for landmark in landmarks:
                lm_x, lm_y = landmarks_to_pixel(landmark, width, height)
                cv2.circle(frame, (lm_x, lm_y), 5, (255, 0, 0), -1)
        if user_answer != "":
            if check_answer(user_answer, correct_answer, current_problem[3]):
                num_correct += 1
                if num_correct < num_questions:
                    current_problem = generate_problem()
                    correct_answer = str(current_problem[2])
                    correct_display_time = time.time() + 1.0
                else:
                    all_correct_message_displayed = True
                    end_display_time = time.time() + 1.0
                user_answer = ""
            else:
                wrong_display_time = time.time() + 1.0
        problem_text = f"{current_problem[0]} {current_problem[3]} {current_problem[1]} = ?"
        frame = display_problem(frame, problem_text)
        if user_answer != "":
            frame = display_user_answer(frame, user_answer)
        frame = display_numbers(frame)
        if time.time() < correct_display_time:
            frame = display_result(frame, "정답이에요!!", (0, 255, 0))
            user_answer = ""
        elif all_correct_message_displayed and time.time() < end_display_time:
            frame = display_end(frame)
        elif time.time() < wrong_display_time:
            frame = display_result(frame, "다시 생각해봐요!", (0, 0, 255))
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()
