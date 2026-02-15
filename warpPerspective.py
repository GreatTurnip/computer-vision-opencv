import cv2
import numpy as np
from utilities import stackImages
path = "resources/chips-are-colored-for-poker-and-playing-cards-on-the-poker-table-poker-casino-win-photo.jpg"
img = cv2.imread(path)
width , height = 250,350
pts1 = np.float32([[54,44], [194,72], [66,202], [176,222]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

for (x,y) in pts1:
    cv2.circle(img,(int(x),int(y)),4,(0,0,255),cv2.FILLED)

result = stackImages([img,output],0.6)
cv2.imshow("Output",result)
cv2.waitKey(0)