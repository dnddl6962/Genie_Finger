from flask import Flask, render_template, Response, request
from tools.mathgame import generate_frames, initialize_hands
from tools.eng1 import generate_english_frames
from tools.eng2 import generate_english2_frames
from tools.maze import generate_maze_frames
from tools.ham import generate_burger_frames
import logging
from datetime import datetime
import os

app = Flask(__name__)

# 로그 설정
log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

# logs 폴더가 없으면 생성
os.makedirs(log_folder, exist_ok=True)

# 현재 날짜를 기준으로 서브디렉터리를 만듭니다.
today_folder = os.path.join(log_folder, datetime.now().strftime('%Y-%m-%d'))

# today_folder가 없으면 생성
os.makedirs(today_folder, exist_ok=True)

log_file_path = os.path.join(log_folder, today_folder, 'server.log')

logging.basicConfig(filename=log_file_path, level=logging.DEBUG)

# Formatter 생성 및 적용
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(log_formatter)

# Root logger에 FileHandler 추가
logging.getLogger().addHandler(file_handler)



@app.route('/')
def security():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('security.html')

@app.route('/index')
def index():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('index.html')

# 수학 컨텐츠 페이지 라우터
@app.route('/math')
def math():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('math.html')

# 영어컨텐츠 페이지 라우터
@app.route('/english')
def eng():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('english.html')

# 이미지 맞추기
@app.route('/eng1')
def eng1():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('eng1.html')

# 영어단어 조합
@app.route('/eng2')
def eng2():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('eng2.html')

# 사고력 컨텐츠 페이지 라우터
@app.route('/thinking_power')
def think():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('think.html')

# 햄버거 만들기
@app.route('/thk1')
def thk1():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('thk1.html')

# 미로 찾기
@app.route('/thk2')
def thk2():
    app.logger.info(f'[{request.method}] {request.path}')
    return render_template('thk2.html')

# 각 컨텐츠 웹캠에서의 이미지 프레임 불러오는 라우터

hands = initialize_hands() # 수학 손 인식   
@app.route('/math_video_feed')
def math_video_feed():
    app.logger.info(f'[{request.method}] {request.path}')
    return Response(generate_frames(hands), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/english1_video_feed')
def english1_video_feed():
    app.logger.info(f'[{request.method}] {request.path}')
    return Response(generate_english_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/english2_video_feed')
def english2_video_feed():
    app.logger.info(f'[{request.method}] {request.path}')
    return Response(generate_english2_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/thinking_power1_video_feed')
def thinking_power1_video_feed():
    app.logger.info(f'[{request.method}] {request.path}')
    return Response(generate_burger_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/thinking_power2_video_feed')
def thinking_power2_video_feed():
    app.logger.info(f'[{request.method}] {request.path}')
    return Response(generate_maze_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

PORT = 5000

if __name__ == '__main__':
    app.logger.info("server on :: PORT="+str(PORT))
    app.run(debug=True, port=PORT)
