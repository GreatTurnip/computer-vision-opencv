import cv2
import numpy as np
img = np.zeros((512,512,3), np.uint8)
print(img)
img[:]=255,0,0
cv2.line(img,(0,0),(255,255),(0,255,0),3)
cv2.rectangle(img,(350,100),(270,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),30,(255,255,255),cv2.FILLED)
cv2.putText(img,"Draw Shapes",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
cv2.imshow("Original",img)
cv2.waitKey(0)