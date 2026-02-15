import cv2
import numpy as np
from utilities import stackImages
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "resources/story_lena_lenna_1.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
stackedImages= stackImages(([img,imgGray,imgBlur],[imgCanny,imgDilation,imgEroded]),0.8)
cv2.imshow("Stack Images",stackedImages)
cv2.waitKey(0)

