import cv2
import numpy as np
def stackImages(imgArray, scale, labels=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])

    sizeW = imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]

    if isinstance(imgArray[0], list):
        for x in range(rows):
            for y in range(cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        hor = [np.hstack(imgArray[x]) for x in range(rows)]
        ver = np.vstack(hor)

    else:
        for x in range(rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        ver = np.hstack(imgArray)

    return ver
