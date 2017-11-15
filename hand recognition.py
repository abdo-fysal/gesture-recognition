import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# take first f`rame of the video
ret,image = cap.read()
hand_classifier=cv2.CascadeClassifier('r.xml')
while(ret):
    ret ,image = cap.read()

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    hands=hand_classifier.detectMultiScale(gray,1.3,5)
    if hands is ():
        print("NO hands found")
    for(x,y,w,h) in hands:
        im=cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
        print(hands)
        cv2.imshow('hand detection',image)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()