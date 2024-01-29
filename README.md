# 코트와 패딩 - Genie Finger

<details>
<summary>🖥 <b>Summary</b></summary><br>
  
### Team Name - 코트와 패딩
### Content Name - Genie Finger
### Team Member & R&R


<table>
  <tr>
    <td align="center">
    <a href="https://github.com/k-3730">
    <img src="https://github.com/k-3730.png" width="150px;" alt="홍준"/>
    <br />
    <sub>
    <b>권홍준</b><br>
    <b> :bulb: PM 및 컨텐츠 개발</b>
    </sub>
    </a>
    <br />
    <td align="center">
    <a href="https://github.com/dony1220">
    <img src="https://github.com/dony1220.png" width="150px;" alt="도현"/>
    <br />
    <sub>
    <b>김도현</b><br>
    <b>🌟 컨텐츠 개발 및 웹 개발</b>
    </sub>
    </a>
    <td align="center">
    <a href="https://github.com/dnddl6962">
    <img src="https://github.com/dnddl6962.png" width="150px;" alt="웅"/>
    <br />
    <sub>
    <b>장 웅</b><br>
    <b>🌟 웹 개발 및 컨텐츠 개발, 로그 연동</b>
    </sub>
    </a>
    <br />
    </td>
    <td align="center">
    <a href="https://github.com/surplus96">
    <img src="https://github.com/surplus96.png" width="150px;" alt="태영"/>
    <br />
    <sub>
    <b>최태영</b><br>
    <b> :bulb: 컨텐츠 개발 및 코드 정제</b>
    </sub>
    </a>
    <br />
    </td>    
    <br />
    </td>
  </tr>
</table>
<br/>


<h3 align="left"><b>🛠 Used Tool/Stack 🛠</b></h3>
</br>
<p align="left">


<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>
<img alt="TensorFlow" src ="https://img.shields.io/badge/TensorFlow-FF6F00.svg?&style=for-the-badge&logo=TensorFlow&logoColor=black"/>
<img alt="Jupyter" src ="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white"/>
<img alt="OpenCV" src ="https://img.shields.io/badge/OpenCV-5C3EE8.svg?&style=for-the-badge&logo=OpenCV&logoColor=white"/>
<img alt="OpenAI" src ="https://img.shields.io/badge/OpenAI-412991.svg?&style=for-the-badge&logo=OpenAI&logoColor=white"/>
<img alt="Anaconda" src ="https://img.shields.io/badge/Anaconda-44A833.svg?&style=for-the-badge&logo=Anaconda&logoColor=black"/>
<img alt="Flask" src ="https://img.shields.io/badge/Flask-000000.svg?&style=for-the-badge&logo=Flask&logoColor=white"/>


<h3 align="left"><b>🛠 Used SCM 🛠</b></h3>
</br>
<p align="left">
<img alt="GitHub" src ="https://img.shields.io/badge/GitHub-181717.svg?&style=for-the-badge&logo=GitHub&logoColor=white"/>
<img alt="Slack" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=for-the-badge&logo=Slack&logoColor=pupple"/>

</details>


- - -
## 📃 **소개**
### **🥇천재교육 빅데이터 5기 '코트와 패딩' Github Page 입니다!🥇**
저희는 유아들을 대상으로 MediaPipe, OpenCV를 이용하여 카메라와 사용자간의 상호작용을 바탕으로 '에듀테인먼트'라는 주제로 프로젝트를 진행하였습니다.
<br>
즉 유아들이 카메라를 통해 게임을 이행하고, 교육에 조금 더 흥미를 높일 수 있도록함이 저희 프로젝트의 궁극적인 목표였습니다.
<br>
<p align="left">
  <img src="https://github.com/dnddl6962/flask/assets/96913965/0af57721-4025-4458-9333-cb2df39dabb8" width = "630px">
</p>

- - -

## **🥑 개발환경 및 운영자 메뉴얼**
<details>
<summary><b>⚓Requirements⚓</b></summary>
  <br>
  1. 주요 개발환경
  <br>
  <br>
    - Flask == 3.0.0
  <br>
    - cvzone == 1.6.1
  <br>
    - mediapipe == 0.10.9
  <br>
    - opencv-contrib-python == 4.9.0.80
  <br>
    - opencv-python == 4.9.0.80
  <br>
    - PyAutoGUI == 0.9.54
  <br>
    - pynput == 1.7.6
  <br>
    - requirements.txt를 별첨하였으며 requirements.txt를 install을 통해 라이브러리를 설치하여 적절하게 환경 Setting이 가능합니다.
  <br>
  <br>
  2. 운영자 메뉴얼
  <br>
  
  - tools 폴더에 담긴 파일에 모든 컨텐츠들이 담겨 있으며, app 파일 하나를 실행했을시에, 돌아갈 수 있도록 분기 처리를 진행하였습니다. 따라서, app.py 코드를 실행하였을 때, 모든 컨텐츠들이 작동하며 app.py 파일에서 Port 번호를 조절하여 User가 사용하는 환경과 상황에 걸맞게 세팅하게끔 설정해 놓았습니다. 뿐만 아니라 Font_path를 커스텀하게 설정해야 합니다.
  
  - 후에 Flask를 실행하면 컨텐츠를 이용할 수 있습니다.

  - 뿐만 아니라, 개인정보동의 항목을 추가하여 사용자가 웹 캠에 나오는 이미지에 대해서 해당 정보와 로그에 대한 개인정보 수용 여부 UI를 보여주며, 동의하면 해당 컨텐츠가 실행될 것이며 동의하지 않을 시 컨텐츠가 종료됩니다.
  </br>
  
</details>

- - -
## **:accessibility: SW License**
<details>
<summary><b>💡License💡</b></summary>
<br>
1. Font : JalnanGothic.TTF
   <p align='left'>
      <img width="400" alt="20231121110245_KakaoTalk_20231120_190823851" src="https://github.com/dnddl6962/flask/assets/96913965/848d1362-738e-4b94-9e19-6356e5380959" width = "630px">
     <br>
     해당 링크를 참조해서 폰트를 다운받아주시고, 라이센스를 참고해주시기 바랍니다.
     <br>
     https://image.goodchoice.kr/images/jalnan_font/jalnan-font-190124ver.pdf
     <br>
     <br>
     
2. MediaPipe : **Apache 2.0 License**
   
   - 해당 라이브러리는 Apache 2.0 License에 의거합니다. 따라서 MediaPipe License를 별첨하였으며 라이센스에 대해서는 해당 파일을 참조하시면 됩니다.
   </p>
   
3. CVZONE : **MIT License**
   - 해당 라이브러리는 MIT License에 의거합니다. 따라서 MIT License를 별첨하였으며 라이센스에 대해서는 해당 파일을 참조하시면 됩니다.
   
4. Flask : **BSD License**
   - 해당 라이브러리는 BSD License에 의거합니다. 따라서 BSD License를 별첨하였으며 라이센스에 대해서는 해당 파일을 참조하시면 됩니다.

5. Pillow : **PIL Software License**
   - 해당 라이브러리는 PIL Software License에 의거합니다. 따라서 PIL Software License를 별첨하였으며 라이센스에 대해서는 해당 파일을 참조하시면 됩니다.

</details>

- - -
## **🧑 컨텐츠 결과**
<details>
<summary><b>🔤English🔤</b></summary>
  <p align='left'>
    <img src = "https://github.com/dnddl6962/flask/assets/96913965/4990cbec-d143-4cbd-945c-44f50d085166" width = "500px">
    <img src = "https://github.com/dnddl6962/flask/assets/96913965/a42a78af-f84e-49d1-b06e-5741318cbd36" width = "500px">
  </p>
</details>

<br>

<details>
<summary><b>💯Math💯</b></summary>
  <p align='left'>
    <img width="400" alt = "math proto" src = "https://github.com/dnddl6962/flask/assets/96913965/160bc60d-0f10-4e02-a5d6-45bfb53c9b36" width = "500px">
</details>

<br>

<details>
<summary><b>🧠Thinking Power🧠</b></summary>
  <p align='left'>
    <img src = "https://github.com/dnddl6962/flask/assets/96913965/620b6f60-cdb1-4db4-9af5-f71c8f35cd0d" width = "500px">
    <img src = "https://github.com/dnddl6962/flask/assets/96913965/d3bb00c8-6222-4ca6-8c9c-812b0c49caad" width = "500px">
  </p>
</details>
