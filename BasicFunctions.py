import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8)
path = "./resources/story_lena_lenna_1.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (9,9),0)
imgCanny = cv2.Canny(img,500,500)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroder = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("Image", img)
cv2.imshow("Image Gray",imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Eroder", imgEroder)
cv2.waitKey(0)