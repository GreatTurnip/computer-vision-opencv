import cv2
frameWidth = 480
frameHeight = 360
cap = cv2.VideoCapture("./resources/sample_960x400_ocean_with_audio.mp4")
while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (frameWidth,frameHeight))
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break