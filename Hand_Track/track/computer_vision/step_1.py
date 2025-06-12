# pip install opencv-python
import cv2

camera = cv2.VideoCapture(0)

while 1:
    _, img = camera.read()

    cv2.imshow("Step 1", img)

    if cv2.waitKey(1) == 27:
        break