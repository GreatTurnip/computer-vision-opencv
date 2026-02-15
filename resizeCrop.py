import cv2
path = "resources/story_lena_lenna_1.jpg"
img = cv2.imread(path)
print(img.shape)
width, height = 400,400
imgResized = cv2.resize(img,(width,height))
print(imgResized.shape)
imgCropped = img[0:512,300:512]
imgCropResized = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
cv2.imshow("Image Resized",imgResized)
cv2.imshow("Original Image",img)
cv2.imshow("Cropped Image",imgCropped)
cv2.imshow("ImageCroppedResized",imgCropResized)
cv2.waitKey(0)