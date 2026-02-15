import cv2
import numpy as np
circles = np.zeros((4,2),np.int32)
counter =0
def mousePoints(event,x,y,flags,param):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter]=x,y
        counter += 1
        print(circles)

path="resources/chips-are-colored-for-poker-and-playing-cards-on-the-poker-table-poker-casino-win-photo.jpg"
img = cv2.imread(path)
cv2.namedWindow("original")
cv2.setMouseCallback("original",mousePoints)
while True:
    imgcpy = img.copy()
    for (x,y) in  circles:
       cv2.circle(imgcpy,(int(x),int(y)),3,(0,0,255),cv2.FILLED)
    if counter == 4:
        width , height = 250,350
        pts1 = np.float32(circles)
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img,matrix,(width,height))

        cv2.imshow("result", output)
    else :
        cv2.imshow("original", imgcpy)
    if cv2.waitKey(1) == 27:
        break
