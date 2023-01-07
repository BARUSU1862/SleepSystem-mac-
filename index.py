import cv2 as cv
import time
import subprocess

HAAR_FILE = "haarcascade_frontalface_default.xml"
cascade = cv.CascadeClassifier(HAAR_FILE)

cap = cv.VideoCapture(0)
noFaceInTheCamera = 0

while(True):
    ret, frame = cap.read()
    face = cascade.detectMultiScale(frame)
    
    for x, y, w, h in face:
        faceNumber =cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        noFaceInTheCamera =0
        
    
    if noFaceInTheCamera > 50:
        subprocess.run(["pmset","sleepnow"])
    
    noFaceInTheCamera = noFaceInTheCamera + 1
    
    cv.imshow('frame',frame)
    time.sleep(0.5)
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv.destroyAllWindows()