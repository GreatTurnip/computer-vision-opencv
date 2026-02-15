from operator import truediv

import cv2
import numpy as np
from utilities import stackImages
path ="./resources/box.mp4"
cap = cv2.VideoCapture(path)
def nothing(x):
    pass
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",(800,600))
cv2.createTrackbar("Threshold1","Parameters",23,255,nothing)
cv2.createTrackbar("Threshold2","Parameters",25,255,nothing)
def getContours(img,imgContour):
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            print(len(approx))
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3)
while True:
    success, img = cap.read()
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    imgContour = img.copy()
    imgblur = cv2.GaussianBlur(img,(7,7),1)
    imgGraY = cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGraY,threshold1,threshold2)
    kernel = np.ones((5,5),np.uint8)
    imgDil = cv2.dilate(imgCanny,kernel,iterations = 1)
    getContours(imgDil,imgContour)
    imgDil = cv2.cvtColor(imgDil, cv2.COLOR_GRAY2BGR)
    imgStack = stackImages([imgContour, imgCanny, imgGraY, imgblur,imgDil,imgDil], 0.5)
    cv2.imshow("Result",imgStack)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()