
# Importing Modules
import cv2
import numpy as np
import os
from tqdm import tqdm

def Crete_Folder_Images(name, directory, tn):
    # Creating directory in the file
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print('DIRECTORY with name %s EXIST'%name)
    # Opening vedio mode with frontal face detector
    faceDetect=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam=cv2.VideoCapture(0)
    size =(100, 100)
    for i in tqdm(range(1, 1+ tn)):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #for GRAY SCALE IMAGES
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        # faces=faceDetect.detectMultiScale(img,1.3,5)    # FOR COLOR IMAGES
        for(x,y,w,h) in faces:
            res = cv2.resize(gray[y:y+h,x:x+w], size, interpolation = cv2.INTER_AREA)
            cv2.imwrite('Datasets/'+str(name)+'/'+str(name)+'_'+str(i)+'.jpg', res)  #for GRAY SCALE IMAGES

            # cv2.imwrite(directory+'/'+str(name)+'-'+str(sn)+'.jpg'
            #             ,img[y:y+h,x:x+w])  # FOR COLOR IMAGES
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(200)
        cv2.imshow('DAtaset Creator',img)
        cv2.waitKey(1)
    cam.release()
    cv2.destroyAllWindows()
    print('TASK COMPLETED')

# Taking inputs

name=input('\nEnter your name: ')

directory='Datasets/'+name
tn= int(input('Enter no.of images to be taken: '))
Crete_Folder_Images(name, directory, tn)
