from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
import cv2,os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from collections import Counter
import sqlite3
from datetime import date,datetime
from testing import post_attendace, check_attendance


tf.keras.backend.clear_session()
# graph = tf.get_default_graph()

app = Flask(__name__)

video_stream = VideoCamera()

VIDEO_TIME=6
STUDENT_ID = None
PERIOD = None
class_labels = {1:'164G1A0571', 2:'164G1A05B0', 4:'164G1A0589', 3:'164G1A0584'}
model = load_model('E:/Project 11/face_model_final.h5', compile=False)



@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
        start=int(datetime.now().strftime("%S"))
        global model, class_labels, STUDENT_ID
        labels = []
        while int(datetime.now().strftime("%S"))-start!=VIDEO_TIME:
                frame = camera.get_frame()
                # plt.imshow(frame)
                nparr = np.fromstring(frame, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                # cv2.imwrite('img'+str(np.random.randint(100*1000))+'.png', img)
                faces=faceDetect.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
                # res = None
                for(x,y,w,h) in faces:
                        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                        res = cv2.resize(gray[y:y+h,x:x+w], (100, 100), interpolation = cv2.INTER_AREA)
                # with graph.as_default():
                labels.append(np.argmax(model.predict(res.reshape(-1, 100, 100, 1).astype(np.float32))))
                yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
        print('*'*11 , ' '*5,max(set(labels), key = labels.count),  class_labels[max(set(labels), key = labels.count)] ,'--', ' '*5, '*'*11)
        STUDENT_ID = max(set(labels), key = labels.count)
        post_attendace(STUDENT_ID)


                

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream), mimetype = 'multipart/x-mixed-replace;boundary=frame')


def get_details():
        global class_labels, PERIOD, STUDENT_ID
        conn = sqlite3.connect('Database.db')
        cur = conn.cursor()
        rollno = class_labels[STUDENT_ID]
        tim = datetime.now().strftime("%H:%M:%S")
        PERIOD = get_period(int(datetime.now().strftime("%H%M")))[1]
        names = {1:'Priya Ranjan', 2:'Syam Kakarla', 3:'Sai Charan', 4:'Sai Rahul'}
        name = names[STUDENT_ID]
        data = [rollno, name, PERIOD, tim]
        for i in data:
                print(i)
        conn.close()
        return data

def get_period(time):
        if time>=int('0930') and time<=int('1020'):
                return 'P1'
        elif time>=int('1021') and time<=int('1110'):
                return 'P2'
        elif time>=int('1121') and time<=int('1210'):
                return 'P3'
        elif time>=int('1211') and time<=int('1300'):
                return 'P4'
        elif time>=int('1400') and time<=int('1450'):
                return 'P5'
        elif time>=int('1451') and time<=int('1540'):
                return 'P6'
        elif time>=int('1541') and time<=int('1630'):
                return 'P7'
        return ' '




@app.route('/submit')
def submit():
    return render_template('submit.htm', data = get_details())


if __name__ == '__main__':
    app.run(debug=True)