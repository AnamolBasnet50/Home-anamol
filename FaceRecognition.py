import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from pyfirmata import Arduino ,SERVO,util
from time import sleep


port = 'COM5'
pin = 8
board=Arduino(port)
board.digital[pin].mode= SERVO



def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.1)
    

def movemotor(name):
    while True:
        rotateservo(pin,angle=120)
        break
    
    

               

            

path = "imageAttendance"
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)


def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        mydatalist = f.readlines()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n {name},{dtString}')




    



encodelistknown = findEncodings(images)
print('encoding complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeface,faceloc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodelistknown,encodeface)
        faceDis = face_recognition.face_distance(encodelistknown,encodeface)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classnames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
            movemotor(name)



    cv2.imshow('face_recognition',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
